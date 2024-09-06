---UZB---
main.py faylni ishlatish uchun sizga kerakli bo'ladigan kutibxonalar:
 
certifi==2024.7.4
charset-normalizer==3.3.2
idna==3.8
pyaes==1.6.1
pyasn1==0.6.0
requests==2.32.3
rsa==4.9
Telethon==1.36.0
urllib3==2.2.2

Bu kutibxonalarni ( pip install -r requirements.txt ) komandasi orqali yuklab olishingiznmumkin.
-----------------------------------------------
config.json faylni o'zingizni shaxsiy ma'lumotlaringizni kiritasiz masalan:

API_ID, API_HASH - Telegram profilingizni ulash uchun kerak kalitlar. Ularni ([my.telegram.org](https://my.telegram.org/auth)) saytidan olishingiz mumkin

PHONE_NUMBER - qismiga telefon raqamizni yozasiz Telegramnikini

SESSION_NAME - qismiga teginishingiz shart emas.

API_KEY - qismiga ([weatherfree](https://www.weatherapi.com/)) saytidan ro'yxatdan o'tib API kalitni olib, o'rniga yozasizlar.
----------------------------------------------
CITY - qismiga siz yashayotgan joyni yozasizlar.

! Shu yerga diqqat bilan qaranh.Telegram profilga faqat 70 ta belgidan oshib ketmaslik kerak. Shuni inobatga olishlar.
-----------------------------------------------
Telegram frofilda ko'rsatiladigan ma'lumotlar:
 
datatime kutibxonasidan:
 Kalendar
 Soat
 
requests kutibxonasidan:
 Mamlakat nomi, ob-havo holati (emoji ko'rinishida), havo harorati, tong otishi va quyosh botishi vaqtlari

Telegram profilning taxminiy o'rinishi:
    📅 2020-02-20 | 🕒 22:02 | Toshkent ☀️ 25.1 °C | 🌅 05:53 AM | 🌇 06:51 PM

---RU---
Чтобы использовать файл, вам понадобятся следующие библиотеки:

certifi==2024.7.4
charset-normalizer==3.3.2
idna==3.8
pyaes==1.6.1
pyasn1==0.6.0
requests==2.32.3
rsa==4.9
Telethon==1.36.0
urllib3==2.2.2

Вы можете загрузить эти библиотеки с помощью команды (pip install -r require.txt).
----------------------------------------------  -
config.json, в который вы вводите свою личную информацию, например:

API_ID, API_HASH — ключи, необходимые для подключения вашего профиля Telegram. Вы можете получить их на (my.telegram.org).

В поле PHONE_NUMBER напишите свой номер телефона или номер Telegram

Вам не нужно менять часть SESSION_NAME.

API_KEY - после регистрации на (weatherfree) сайте возьмите API ключ и пропишите его.
-----------------------------------------------
В разделе CITY напишите место, где вы живете.

! Посмотрите внимательно здесь. Профиль Telegram не должен превышать 70 символов. Примите это во внимание.
