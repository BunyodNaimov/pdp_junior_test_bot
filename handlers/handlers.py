import os

from aiogram import types, Router, F
from aiogram.types import FSInputFile

from handlers.keyboards import kurslarimiz, start_buttons

router = Router()

@router.message(F.text == "Kompaniya haqida")
async def get_about_company(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    text = "8 yillik tajribaga, 2000 dan ortiq o'quvchilar va tajribali mentorlarga ega!"
    await msg.answer_photo(photo=company_image, caption=text)

@router.message(F.text == "Bizning Mentorlar")
async def get_mentorlar(msg: types.Message):
    img1 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_3.png"))
    img2 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_4.png"))
    img3 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_5.png"))
    mentorlar = [
        [img1, "Habibulla Nuridinov"],
        [img2, "Asilbek Mamadaliyev"],
        [img3, "Shohruh Abdurahmonov"],
    ]
    for mentor in mentorlar:
        await msg.answer_photo(photo=mentor[0], caption=mentor[1])

@router.message(F.text == "Kurslarimiz")
async def get_kurslarimiz(msg: types.Message):
    await msg.answer(text='Bizning kurslarimiz', reply_markup=kurslarimiz)

@router.message(F.text == "Python Junior")
async def get_python_junior(msg: types.Message):
    python_img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_6.png"))
    await msg.answer_photo(photo=python_img,caption='Python Junior')

@router.message(F.text == "Frontend Junior")
async def get_python_junior(msg: types.Message):
    frontend_img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_7.png"))
    await msg.answer_photo(photo=frontend_img,caption='Frontend Junior')

@router.message(F.text == "Robototexnika")
async def get_python_junior(msg: types.Message):
    robo_img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_8.png"))
    await msg.answer_photo(photo=robo_img,caption='Robototexnika')

@router.message(F.text == "Scratch")
async def get_python_junior(msg: types.Message):
    scratch_img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_9.png"))
    await msg.answer_photo(photo=scratch_img,caption='Scratch')

@router.message(F.text == "🔙Ortga")
async def back_btn(msg: types.Message):
    await msg.answer(text="Ortga", reply_markup=start_buttons)