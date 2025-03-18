import os

from aiogram import types, Router, F
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text == "Kompaniya haqida")
async def get_about_company(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    text = "8 yillik tajribaga, 2000 dan ortiq o'quvchilar va tajribali mentorlarga ega!"
    await msg.answer_photo(photo=company_image, caption=text)
