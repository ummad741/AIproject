from aiogram.types import Message, ContentType
from aiogram import Router
from aiogram.filters import CommandStart
from generators.openai import *

router = Router()
admin_router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Assalomu alekum botga hush kelibsiz")

@router.message(content_types=ContentType.TEXT)
async def handle_message(message: Message):
    user_question = message.text
    answer = await ask_gpt(user_question)
    await message.reply(answer)
