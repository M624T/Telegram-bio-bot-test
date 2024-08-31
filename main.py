import json
import requests
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

# config.json faylidan ma'lumotlarni o'qish
def read_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

config = read_config('config.json')

# Telegram API uchun ma'lumotlarni json faylidan olib qo'yish
api_id = config['API_ID']
api_hash = config['API_HASH']
phone_number = config['PHONE_NUMBER']
session_name = config['SESSION_NAME']
api_key = config['API_KEY']
city = config['CITY']

client = TelegramClient(session_name, api_id, api_hash) # Telegram API uchun client yaratish

async def update_profile():
    while True:
        now_data = datetime.now().strftime('%Y-%m-%d') #  hozirgi sana
        now_time = datetime.now().strftime('%H:%M')  # hozirgi vaqti

        # Ob-havo ma'lumotini URL bilon forecast.json fayli orqali olish
        url_forecast = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no"
        forecast = requests.get(url_forecast)
        weather_day_info = forecast.json() # Ob-havo ma'lumotlarini json formatida olish
        sunrise = weather_day_info['forecast']['forecastday'][0]['astro']['sunrise'] # Ob-Havo tong otish vaqti
        sunset  = weather_day_info['forecast']['forecastday'][0]['astro']['sunset'] #  Ob-Havo quyosh botish vaqti

        # Ob-havo ma'lumotini URL bilon current.json fayli orqali olish
        url_current = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        current = requests.get(url_current)
        weather_data = current.json() # Ob-havo ma'lumotlarini json formatida olish
        temperature = weather_data['current']['temp_c'] # Ob_Havo haroratini olish °C ko'rinishida
        condition = weather_data['current']['condition']['text'].lower() # Ob-Havo holatini bilish
        region = weather_data['location']['region'] # Mamlakat nomini olish

        # Ob-Havo holatini str holatidan Emoji ko'rinishida saqlaymiz
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
            emoji = "🌡️"

        # Telegramg profilga yozilishi kerak bo'lgan matn
        about_text = f"📅 {now_data} | 🕒 {now_time} | {region} {emoji} {temperature} °C | 🌅 {sunrise} | 🌇 {sunset}"

        # Matn uzunligini tekshirish va kerak bo'lsa qisqartirish
        max_length = 70
        if len(about_text) > max_length:
            about_text = about_text[:max_length]

        await client(UpdateProfileRequest(about=about_text)) # Matnni Telegram (bio) ga yuklaymiz
        print(f"({now_time}) Profil bio yangilandi --> {about_text}") # Terminalda bio yangilangaanligini ko'rish uchun
        await asyncio.sleep(600)  # Har 600 sekund ( 10-minut )da bir marta yangilanish

async def main():
    await client.start(phone=phone_number)
    await update_profile()

with client:
    client.loop.run_until_complete(main())
