from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Assalomu alekum botga hush kelibsiz")
