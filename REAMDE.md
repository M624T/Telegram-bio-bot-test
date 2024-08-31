```
config.json fayliga yozilishi kerak bo'lgan ko'rsatkichlar
--------------------------------
API_ID va API_HASH manashu -> https://my.telegram.org/auth
saytdan olasiz

session_name = o'zgartirish keragi yo'q, shunchaki registratsiyada qaytadan o'tmaslik uchun

Telefon nomerni o'zingiznikini yozasiz.

API_KEY = https://www.weatherapi.com/  saytdan registratsiyadan o'tib API kalitni olasiz

va ( "CITY": "Tashkent" ) deb yozasiz

--------------------------------
Ishlatish shart emas lekin maslahat beriladigan qismi
--------------------------------

Venv orqali ishlatishingizni maslahat beraman
Terminalga kirib (main.py) faylni yoniga borasiz va [python -m venv venv] terminalga yozasiz
Keyin .\venv\Script\python.exe  faylini ishga tushirasiz
ishga tushganidan so'ng [pip install -r requirements.txt] yozasiz
Keyin main.py faylni ishga tushasiz
----------------------------------
Kerakli kutibxona busiz ishlamaydi
---------------------------------

pip install telethon
pip install requests

yoki terminalga kirib main.py faylni papkasiga borib, manabu komandanii yozing [ pip install -r requirements.txt ]
```