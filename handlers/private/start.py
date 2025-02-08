from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from magic_filter import F

from data.config import CHANNELS
from keyboards.default.user_dbuttons import user_main_dbuttons
from utils.user_functions import logging_text

from loader import dp, db, bot


async def send_welcome_message(message: types.Message):
    first_channel = await bot.get_chat(CHANNELS[0])
    second_channel = await bot.get_chat(CHANNELS[1])

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text=first_channel.full_name, url=f"https://t.me/{first_channel.username}"),
        types.InlineKeyboardButton(text=second_channel.full_name, url=f"https://t.me/{second_channel.username}"),
        types.InlineKeyboardButton(text="✅ A'zo bo'ldim!", callback_data="subscribed")
    )
    await message.answer(
        "Tabriklaymiz!!! Siz birinchi qadamni bosdingiz! Davom etish uchun quyidagi kanallarimizga a'zo bo'ling.\n\n"
        "Keyin \"✅ А'zo bo'ldim!\" tugmasini bosing",
        reply_markup=markup
    )


@dp.message_handler(F.text == "/bekor", state="*")
async def bekor_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Jarayon bekor qilindi!", reply_markup=user_main_dbuttons)


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()

    try:
        await send_welcome_message(message)
        # await message.answer(text=f"Assalomu alaykum! {message.from_user.full_name}", reply_markup=user_main_dbuttons)
        await db.add_user(message.from_user.id)
    except Exception as err:
        await logging_text(err)

@dp.message_handler(F.text == "Bosh sahifa", state="*")
async def user_main_page(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=user_main_dbuttons
    )