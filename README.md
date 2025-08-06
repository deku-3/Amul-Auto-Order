# 🥛💪 Amul Protein Auto-Order Bot

Beat the protein rush and automatically order from Amul before anyone else can!  
This bot monitors stock, orders the product for you, and notifies you via UPI request.

---

## Features

- **Instant auto-ordering:** Refreshes & orders as soon as stock appears.
- **Login session saver:** No repeated OTP hassle.
- **UPI payment push:** Approve the order from your phone.
- **Adjustable refresh interval:** Perfect your buy timing.

---

## Quickstart

### 0️⃣ Clone this repository

git clone https://github.com/deku-3/Amul-Auto-Order.git
cd Amul-Auto-Order

## 🔐 1) Save Your Browser Session

Run the session saver to store your login state:



python save_sessions.py

- A dummy browser window will open.
- Enter your **pincode**, **phone number**, and the OTP you receive.
- If prompted, fill in your name/email, then **press ENTER** in the terminal.
- This will save a file called `auth.json` containing your cookies, headers, and session state.

✅ _You’re doing this so the script can later impersonate a logged-in, OTP-authenticated user._

---

## 🏠 2) Add Your Address

- In your real browser:
  - Log in with the **same phone/email** you used in Step 1.
  - Go to your profile and **add an address**.
- ⚠️ _The script will fail if no address is present!_

---

## ⚙️ 3) Configure Your Product & Payment

1. Open `config.py` and fill in the following:

   - **PRODUCT_URL:** Paste the full URL of your Amul product page.
   - **UPI_ID:** Your UPI ID _before_ the `@` symbol (e.g., `adityakumar123` if your UPI is `adityakumar123@okaxis`)
   - **UPI_AFTER_AT:** The part _after_ `@` (e.g., `okaxis`)
   - **UPI_SERVICE:** Your UPI app name (preferably `"Google Pay"` as it's tested)
   - **REFRESH_INTERVAL:** How often (in seconds) the script checks for product availability

2. **Save the file.**

---

## 🚀 4) Start the Watchdog

Make sure:
- Your **cart is empty**
- Your **address is added**

Then run:

python amul_watchdog.py


- The script will now stay live, checking availability on your chosen product page.
- When the product drops, you’ll get a notification on your phone to enter your UPI PIN and complete the order!
