from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from .keyboards import company_about
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=company_about)