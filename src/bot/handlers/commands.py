from aiogram.types import Message, ContentType
from aiogram import Router
from aiogram.filters import CommandStart
# from aiogram.fsm import FsmContext
from aiogram import F

# local files
from bot.generators.openai import chat_gpt
from bot.states.fsmstates import GenerationStates

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Assalomu alekum botga hush kelibsiz")

@router.message()
async def generate_answer(message: Message):
    # prompt=message.text
    gpt_answer = chat_gpt(message.text)
    print(gpt_answer)
    await message.answer(gpt_answer['result'])