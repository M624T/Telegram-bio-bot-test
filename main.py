import os
from dotenv import load_dotenv
import signal
import sys
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
session_name = 'session_name'

# Sessiya faylini o'chirish
session_file = f'{session_name}.session'

def cleanup(signal_received, frame):
    """O'chirish funksiyasi: signalni qabul qiladi va sessiya faylini o'chiradi."""
    print("Dastur to'xtatilyapti...")
    if client.is_connected():
        client.disconnect()  # TelegramClient-ni uzish
        client.session.close()  # Sessiyani yopish
    if os.path.exists(session_file):
        os.remove(session_file)
        print(f'{session_file} fayli o\'chirildi.')
    sys.exit(0)

# Signalni qabul qilish
signal.signal(signal.SIGINT, cleanup)  # Ctrl+C (SIGINT) signalini qabul qilish
signal.signal(signal.SIGTERM, cleanup)  # Terminate signal (SIGTERM) qabul qilish

client = TelegramClient(session_name, api_id, api_hash)

async def update_profile():
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Emoji qo'shish
        about_text = f"🕒 Hozir: {now} 🔰"
        await client(UpdateProfileRequest(about=about_text))
        print(f"Profil bio yangilandi: {about_text}")
        await asyncio.sleep(30)  # Har 30 sekundda bir marta yangilanish

async def main():
    await client.start(phone=phone_number)
    await update_profile()  # Profilni yangilashni boshlash

with client:
    client.loop.run_until_complete(main())
