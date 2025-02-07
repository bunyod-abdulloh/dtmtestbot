from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from magic_filter import F
from utils.user_functions import logging_text
from keyboards.default.user_dbuttons import user_main_dbuttons

from loader import dp, db


@dp.message_handler(F.text == "/bekor", state="*")
async def bekor_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Jarayon bekor qilindi!", reply_markup=user_main_dbuttons)


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()

    try:
        await message.answer(text=f"Assalomu alaykum! {message.from_user.full_name}", reply_markup=user_main_dbuttons)
        await db.add_user(message.from_user.id)
    except Exception as err:
        await logging_text(err)


@dp.message_handler(F.text == "Bosh sahifa")
async def user_main_page(message: types.Message, state: FSMContext):
    await bot_start(message, state)
