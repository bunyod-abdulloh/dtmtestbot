from aiogram import types
from magic_filter import F

from keyboards.default.user_dbuttons import biology_dtm_dbuttons, biology_sert_dbuttons
from loader import dp


@dp.message_handler(F.text == "📚 Kimyo DTM Testlar")
async def handle_biology_dtm(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=biology_dtm_dbuttons
    )


# Testlar e kirill a kirillda | Chemistry dtm
@dp.message_handler(F.text == "📌 Tеstlаr varianti (PDF)")
async def handle_biology_dtm_pdf(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )


@dp.message_handler(F.text == "▶️ Test ishlash (Biologiya DTM)")
async def handle_biology_dtm_play(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!", reply_markup=biology_sert_dbuttons
    )


@dp.message_handler(F.text == "📚 Biologiya Milliy Sertifikat Testlar")
async def handle_biology_sert(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=biology_sert_dbuttons
    )


# Testlar e lotin a kirillda | Chemistry sertifikat
@dp.message_handler(F.text == "📌 Tеstlar varianti (PDF)")
async def handle_biology_sert_pdf(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )


@dp.message_handler(F.text == "▶️ Test ishlash (Biologiya Milliy Sertifikat)")
async def handle_biology_sert_play(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )
