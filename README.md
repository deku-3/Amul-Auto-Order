🥛💪 Beat the Protein Rush
Auto-order Amul with unfair speed — place your order in seconds before anyone else can even click “Add to Cart.”

🤖 Hungry for protein? Follow these steps and beat the chase:
⚠️ Prerequisite: Bring the code to your local machine before proceeding.

0️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/amul-autobuy.git
cd amul-autobuy
1️⃣ Run the session saver
bash
Copy
Edit
python save_sessions.py
This opens a dummy browser.

Enter your pincode, phone number, and the OTP.

(Optional) Add your name/email if prompted.

Press Enter in the terminal once done.

✅ This will create an auth.json file containing your cookies, headers, and login state.
📌 This saved state tricks the Amul website into thinking you're already logged in next time — no OTP needed.

2️⃣ Add your address in browser
Open your real browser (e.g., Chrome).

Log in to Amul using the same phone/email as Step 1.

Click on your profile, and add a delivery address manually.

⚠️ The code will fail if no address is saved.

3️⃣ Configure your order
Open config.py and fill in:

Variable	What to add
PRODUCT_URL	URL of the product you want to auto-order
UPI_ID	Your UPI ID (before the @)
UPI_AFTER_AT	UPI service name (after the @) e.g. okaxis, oksbi
UPI_SERVICE	The UPI app name on your phone — e.g. Google Pay
REFRESH_INTERVAL	Number of seconds between refresh checks (e.g. 2)

🛠️ Example:

python
Copy
Edit
PRODUCT_URL = "https://shop.amul.com/product/amul-protein-shake"
UPI_ID = "yourusername"
UPI_AFTER_AT = "oksbi"
UPI_SERVICE = "Google Pay"
REFRESH_INTERVAL = 2
4️⃣ Start the bot and wait
Make sure your cart is empty and address is set, then run:

bash
Copy
Edit
python amul_watchdog.py
🟢 This script will:

Stay live in terminal

Refresh the product page every few seconds

Auto-order the product as soon as it's in stock

Trigger a UPI notification on your phone to complete the payment

📲 Notification Preview
When your product is in stock, you'll instantly get a UPI notification like this:
