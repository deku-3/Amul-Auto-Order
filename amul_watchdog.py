# amul_watchdog.py
import time
from playwright.sync_api import sync_playwright
from amul_order import order_with_saved_session  # 👈 Make sure this file exists
from config import PRODUCT_URL
ADD_TO_CART_SELECTOR = "a.add-to-cart"
CHECK_INTERVAL = 60  # seconds

def check_stock_loop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        while True:
            try:
                page.goto(PRODUCT_URL, timeout=15000)
                page.wait_for_selector(ADD_TO_CART_SELECTOR, timeout=5000)
                button = page.query_selector(ADD_TO_CART_SELECTOR)
                disabled = button.get_attribute("disabled")

                print(f"[{time.ctime()}] Stock Status: disabled = {disabled}")

                if disabled == "true":
                    print("✅ Product is now in stock. Starting order...")
                    break
                else:
                    print(f"❌ Still out of stock. Retrying in {CHECK_INTERVAL} sec.")
            except Exception as e:
                print("⚠️ Error during check:", e)

            time.sleep(CHECK_INTERVAL)

    # 🟢 Now start the ordering process
    order_with_saved_session()

if __name__ == "__main__":
    check_stock_loop()
