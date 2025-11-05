import asyncio
from telegram import Bot
from datetime import datetime
import time

TOKEN = "8173442296:AAG-RGWLDPH4Pe8qcDfijmmTafMVOVIdaT4"
CHAT_ID = "5772256620"
bot = Bot(token=TOKEN)

async def send_daily_message():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"📅 امروز {now}\nیادت نره کارهای امروز رو انجام بدی 💪"
    await bot.send_message(chat_id=CHAT_ID, text=message)
    print("✅ پیام با موفقیت ارسال شد!")

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == "10:38":  # هر زمان خواستی بذار
        asyncio.run(send_daily_message())
        time.sleep(60)
    time.sleep(10)