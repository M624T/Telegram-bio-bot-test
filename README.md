main.py faylni ishlatish uchun sizga kerakli bo'ladigan kutibxonalar:

* certifi==2024.7.4
* charset-normalizer==3.3.2
* idna==3.8
* pyaes==1.6.1
* pyasn1==0.6.0
* requests==2.32.3
* rsa==4.9
* Telethon==1.36.0
* urllib3==2.2.2

Bu kutibxonalarni (pip install -r requirements.txt) komandasi orqali yuklab olishingiz mumkin.

-----------------------------------------------

config.json faylni o'zingizni shaxsiy ma'lumotlaringizni kiritasiz masalan:

* API_ID, API_HASH - Telegram profilingizni ulash uchun kerak kalitlar. Ularni ([my.telegram.org](https://my.telegram.org/auth)) saytidan olishingiz mumkin
* PHONE_NUMBER - qismiga telefon raqamizni yozasiz Telegramnikini
* SESSION_NAME - qismiga teginishingiz shart emas
* API_KEY - qismiga ([weatherfree](https://www.weatherapi.com/)) saytidan ro'yxatdan o'tib API kalitni olib, o'rniga yozasizlar
* CITY - qismiga siz yashayotgan joyni yozasizlar

! Shu yerga diqqat bilan qaranh. Telegram profilga faqat 70 ta belgidan oshib ketmaslik kerak. Shuni inobatga olishlar.

-----------------------------------------------

Telegram frofilda ko'rsatiladigan ma'lumotlar:

* datatime kutibxonasidan:
	+ Kalendar
	+ Soat
* requests kutibxonasidan:
	+ Mamlakat nomi
	+ Ob-havo holati (emoji ko'rinishida)
	+ Havo harorati
	+ Tong otishi va quyosh botishi vaqtlari

Telegram profilning taxminiy o'rinishi:
    📅 2020-02-20 | 🕒 22:02 | Toshkent ☀️ 25.1 °C | 🌅 05:53 AM | 🌇 06:51 PM

------------------------RU------------------------

Давайте использовать файл, вам понадобятся следующие библиотеки:

* certifi==2024.7.4
* charset-normalizer==3.3.2
* idna==3.8
* pyaes==1.6.1
* pyasn1==0.6.0
* requests==2.32.3
* rsa==4.9
* Telethon==1.36.0
* urllib3==2.2.2

Вы можете загрузить эти библиотеки с помощью команды (pip install -r require.txt).

-----------------------------------------------

config.json, в который вы вводите свою личную информацию, например:

* API_ID, API_HASH — ключи, необходимые для подключения вашего профиля Telegram. Вы можете получить их на ([my.telegram.org](https://my.telegram.org/auth))
* PHONE_NUMBER — номер телефона или номер Telegram
* SESSION_NAME — не изменяйте эту часть
* API_KEY — после регистрации на ([weatherfree](https://www.weatherapi.com/)) сайте возьмите API ключ и пропишите его
* CITY — место, где вы живете

! Посмотрите внимательно здесь. Профиль Telegram не должен превышать 70 символов. Примите это во внимание.

-----------------------------------------------

Информация, отображаемая в профиле Telegram:

* из библиотеки datetime:
	+ Календарь
	+ Время
* из библиотеки requests:
	+ Название страны
	+ Состояние погоды (в виде эмодзи)
	+ Температура
	+ Время восхода и захода солнца

Примерный вид профиля Telegram:
    📅 2020-02-20 | 🕒 22:02 | Ташкент ☀️ 25.1 °C | 🌅 05:53 AM | 🌇 06:51 PM
