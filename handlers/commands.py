import os

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from .keyboards import start_buttons
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_1.png"))
    text = "Assalomu Aleykum Pdp Junior botiga xush kelibsiz!"
    await message.answer_photo(photo=img,caption=text, reply_markup=start_buttons)