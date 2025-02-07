from aiogram import types
from magic_filter import F

from keyboards.default.user_dbuttons import chemistry_dtm_dbuttons, chemistry_sert_dbuttons
from loader import dp


@dp.message_handler(F.text == "📚 Kimyo DTM Testlar")
async def handle_chemistry_dtm(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=chemistry_dtm_dbuttons
    )


@dp.message_handler(F.text == "📌 Testlar varianti (PDF)")
async def handle_chemistry_dtm_pdf(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )


@dp.message_handler(F.text == "📚 Kimyo Milliy Sertifikat Testlar")
async def handle_chemistry_ms(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=chemistry_sert_dbuttons
    )
