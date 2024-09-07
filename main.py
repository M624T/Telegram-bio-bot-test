import json
import requests
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

# config.json faylidan ma'lumotlarni o'qish
def read_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

config = read_config("config.json")

tsikl = 0  # Telegram profil nechi marta o'zgartirilganligini hisoblash uchun

# Telegram API uchun ma'lumotlarni json faylidan olib qo'yish
api_id = config["API_ID"]
api_hash = config["API_HASH"]
phone_number = config["PHONE_NUMBER"]
session_name = config["SESSION_NAME"]
api_key = config["API_KEY"]
city = config["CITY"]

client = TelegramClient(
    session_name, api_id, api_hash
)  # Telegram API uchun client yaratish


async def update_profile():
    global tsikl  # tsikl o'zgaruvchisiga global deb e'lon qilish
    
    while True:
        now_data = datetime.now().strftime("%Y-%m-%d")  # hozirgi sana
        now_time = datetime.now().strftime("%H:%M")  # hozirgi vaqt

        # Ob-havo ma'lumotini URL bilan forecast.json fayli orqali olish
        url_forecast = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no"
        forecast = requests.get(url_forecast)
        weather_day_info = forecast.json()  # Ob-havo ma'lumotlarini json formatida olish
        sunrise = weather_day_info["forecast"]["forecastday"][0]["astro"]["sunrise"]  # Ob-Havo tong otish vaqti
        sunset = weather_day_info["forecast"]["forecastday"][0]["astro"]["sunset"]  # Ob-Havo quyosh botish vaqti

        # Ob-havo ma'lumotini http client orqali kirish
        url_current = (
            f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        )
        current = requests.get(url_current)
        weather_data = current.json()  # Ob-havo ma'lumotlarini currentjson formatida olish
        temperature = weather_data["current"]["temp_c"]  # Ob-Havo haroratini hozirgi vaqtda °C ko'rinishida olish
        condition = weather_data["current"]["condition"]["text"].lower()  # Ob-Havo holatini hozirgi vaqtda bilish
        region = weather_data["location"]["region"]  # Mamlakat nomini olish

        # Ob-Havo holatini (str) holatidan Emoji ko'rinishida saqlaymiz
        emoji = ""
        if "sunny" in condition:
            emoji = "☀️"
        elif "cloud" in condition:
            emoji = "☁️"
        elif "rain" in condition or "shower" in condition:
            emoji = "🌧️"
        elif "snow" in condition:
            emoji = "❄️"
        elif "storm" in condition or "thunder" in condition:
            emoji = "⛈️"
        else:
            emoji = "🌡️"  # Agar hechqaysi havo holati to'g'ri kelmasa

        # Telegramg profilga yozilishi kerak bo'lgan matn
        about_text = f"📅 {now_data} | 🕒 {now_time} | {region} {emoji} {temperature} °C | 🌅 {sunrise} | 🌇 {sunset}"

        # Matn uzunligini tekshirish va kerak bo'lsa qisqartirish
        max_length = 70
        if len(about_text) > max_length:
            about_text = about_text[:max_length]

        tsikl += 1  # O'zgaruvchini oshirish

        await client(UpdateProfileRequest(about=about_text))  # Matnni Telegram (bio) ga yuklaymiz
        print(f"🔄 {tsikl} - aylana ({now_time})\n    Profil bio yangilandi --> {about_text}")  # Terminalda bio yangilangaanligini ko'rish uchun
        await asyncio.sleep(600)  # Har 600 sekund ( 10-minut )da bir marta yangilanish


async def main():
    await client.start(phone=phone_number)
    await update_profile()

# Xatolikni boshqaruvchi qism
try:
    with client:
        client.loop.run_until_complete(main())
except ConnectionError:
    print("------------------------------------")
    print("(ENG)\t❌ Internet connection problem.")
    print("(RU)\t❌ Проблема подключения к интернету.")
    print("(UZB)\t❌ Internetga ulanishda muammo.")
    print("------------------------------------")
except KeyboardInterrupt:
    print("------------------------------------")
    print("(ENG)\t❌ Program ended.")
    print("(RU)\t❌ Программа завершилась.")
    print("(UZB)\t❌ Dastur yakunlandi.")
    print("------------------------------------")
except Exception as e:
    print("------------------------------------")
    print(f"(ENG)\t❌ An error occurred: {e}")
    print(f"(RU)\t❌ Произошла ошибка: {e}")
    print(f"(UZB)\t❌ Xatolik yuz berdi: {e}")
    print("------------------------------------")
