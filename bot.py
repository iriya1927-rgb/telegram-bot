
import sqlite3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8330008814:AAFy8Pg23dTYidV3M7wxMjCTHqw7p0w5HXE"

# Database setup
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    referrer_id INTEGER,
    referrals INTEGER DEFAULT 0
)
""")
conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()

    if not user:
        referrer_id = None

        if context.args:
            try:
                referrer_id = int(context.args[0])
            except:
                referrer_id = None

        cursor.execute("INSERT INTO users (user_id, referrer_id) VALUES (?, ?)", (user_id, referrer_id))
        conn.commit()

        # Increase referral count
        if referrer_id:
            cursor.execute("UPDATE users SET referrals = referrals + 1 WHERE user_id=?", (referrer_id,))
            conn.commit()

    referral_link = f"https://t.me/{context.bot.username}?start={user_id}"

    cursor.execute("SELECT referrals FROM users WHERE user_id=?", (user_id,))
    referrals = cursor.fetchone()[0]

    await update.message.reply_text(
        f"👋 Welcome!\n\n"
        f"🔗 Your Referral Link:\n{referral_link}\n\n"
        f"👥 Total Referrals: {referrals}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling ()
