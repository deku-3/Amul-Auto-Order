from playwright.sync_api import sync_playwright

def save_amul_login_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Open browser with UI
        context = browser.new_context()
        page = context.new_page()

        # Go to a page that will trigger login
        page.goto("https://shop.amul.com/en/checkout")

        print(" Please log in manually:")
        print(" Enter your phone number, receive OTP, and complete login.")
        input(" Press ENTER here ONLY after you're fully logged in.")

        # Save session to file
        context.storage_state(path="auth.json")
        print(" Session saved to 'auth.json'. Use it in your automation scripts.")
        browser.close()

save_amul_login_session()
