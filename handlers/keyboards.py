from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

about_company = KeyboardButton(text="Kompaniya haqida")
mentorlar = KeyboardButton(text="Bizning Mentorlar")
kurslar = KeyboardButton(text="Kurslarimiz")
contact = KeyboardButton(text="Kontaktlar/Manzil")
language = KeyboardButton(text="uzb/eng Til")
start_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [about_company, mentorlar],
        [kurslar],
        [contact, language]
    ], resize_keyboard=True
)