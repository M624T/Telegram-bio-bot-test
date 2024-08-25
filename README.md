Telegram Profil Bio-ni Muntazam Yangilash
Ushbu Python skript Telethon kutubxonasidan foydalanib, Telegram profilingizning bio qismini har 30 soniyada avtomatik yangilab turadi. Skript joriy vaqtni o'z ichiga olgan matnni bio qismiga qo'shib, profilingizni doimiy ravishda yangilab turadi.

O'rnatish
Dastlab, kerakli kutubxonani o'rnating:

bash
Копировать код
pip install telethon
Foydalanish
API ma'lumotlari: api_id, api_hash, va phone_number qiymatlarini Telegramdan olganingizdan keyin .py faylga kiriting.

Skriptni ishga tushirish: Skriptni ishga tushirish uchun:

bash
Копировать код
python script_name.py
Sessiyani boshqarish: Skript ishlash vaqtida sessiya fayli (session_name.session) yaratiladi. Skript to'xtatilganda, sessiya fayli avtomatik ravishda o'chiriladi.

Signalni qayta ishlash: Skriptni to'xtatishda (Ctrl+C) Telegram mijozidan to'g'ri uzilish va sessiya faylini o'chirish ta'minlanadi.

Moslashtirish
Yangilanish intervali: Agar bio yangilanish tezligini o'zgartirmoqchi bo'lsangiz, asyncio.sleep(30) qatoridagi 30 soniyani o'zingizga mos bo'lgan qiymatga o'zgartiring.
Bio matni: about_text o'zgaruvchisini o'zgartirib, bio matniga qo'shimcha ma'lumotlar yoki emojilar kiritishingiz mumkin.
Hujjatlar
Qo'shimcha ma'lumotlar uchun Telethon hujjatlariga murojaat qiling.
