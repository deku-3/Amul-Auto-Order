from playwright.sync_api import sync_playwright
import time
from config import PRODUCT_URL,UPI_ID,UPI_AFTER_AT,UPI_SERVICE
def order_with_saved_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        try:
            context = browser.new_context(storage_state="auth.json")
        except Exception as e:
            print("❌ Failed to load saved session:", e)
            return

        page = context.new_page()

        # Step 1: Go to product page
        try:
            page.goto(PRODUCT_URL)
            print("🛍️ Navigated to product page.")
        except Exception as e:
            print("❌ Failed to open product page:", e)

        # Step 2: Add to cart
        try:
            page.wait_for_selector("a.add-to-cart:not([disabled])", timeout=10000)
            page.click("a.add-to-cart")
            print("🛒 Product added to cart.")
        except Exception as e:
            print("❌ Failed to add product to cart:", e)


        # Step 3: Go to checkout
        try:
            page.goto("https://shop.amul.com/en/checkout")
            page.wait_for_load_state("networkidle")
            print("✅ Navigated to checkout page.")
        except Exception as e:
            print("❌ Failed to go to checkout:", e)

        # Step 4: Ship to this address
        try:
            page.click("button:has-text('Ship To This Address')")
            print("🚚 Clicked 'Ship To This Address'")
        except Exception as e:
            print("⚠️ Address confirmation step skipped or failed:", e)

        # Step 4.2: select phone pay
        try:
            # Option 1: Click the span text "Phone Pe"
            page.click("text=Phone Pe", timeout=5000)
            print("✅ 'Phone Pe' payment option selected.")
        except Exception as e:
            print("❌ Failed to select 'Phone Pe' option by text:", e)

        # Step 5: Click Pay Now
        try:
            page.wait_for_selector("button:has-text('Pay Now')", timeout=5000)
            page.click("button:has-text('Pay Now')")
            print("💳 'Pay Now' clicked — waiting for payment options...")
        except Exception as e:
            print("❌ Failed to click 'Pay Now':", e)

        # Step 6: Select UPI payment method
        try:
            page.wait_for_selector("input#new-vpa", timeout=10000)
            page.check("input#new-vpa")
            print("✅ UPI payment method selected.")
        except Exception as e:
            print("❌ Failed to select UPI payment method:", e)

        # Step 7: Click Google Pay tab
        try:
            page.click(f"text={UPI_SERVICE}")  # May vary — selector can be adjusted
            print("✅ Google Pay tab selected.")
        except Exception as e:
            print("⚠️ Could not switch to Google Pay tab (may already be selected):", e)

        # Step 8: Fill UPI ID and select suffix
        try:
            page.fill("input[placeholder='UPI ID']", UPI_ID)
            page.select_option("select", value=UPI_AFTER_AT)
            print("✍️ UPI ID and suffix filled.")
        except Exception as e:
            print("❌ Failed to fill UPI ID:", e)

        # Step 9: Click 'VERIFY UPI ID'
        try:
            page.wait_for_selector("a.inline-input-btn", timeout=5000)
            page.click("a.inline-input-btn")
            print("🔍 Clicked 'VERIFY UPI ID'.")
        except Exception as e:
            print("❌ Failed to verify UPI ID:", e)

        # Step 10: Click 'PAY'
        time.sleep(1) #necesary to ensure UPI id is verified, IF your internet is slow you can make it 2 or 3 seconds
        try:
            page.wait_for_selector("button:has-text('PAY')", timeout=5000)
            page.click("button:has-text('PAY')")
            print("✅ PAY button clicked — payment initiated.")
        except Exception as e:
            print("❌ Failed to click PAY button:", e)

        # Final Step: Wait and close
        time.sleep(60)
        print("✅ Script complete. Closing browser.")
        browser.close()

# To run:
# order_with_saved_session()
