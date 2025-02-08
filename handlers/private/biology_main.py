from aiogram import types
from magic_filter import F

from handlers.private.chemistry_main import send_doc_to_user
from keyboards.default.user_dbuttons import biology_dtm_dbuttons, biology_sert_dbuttons
from loader import dp


@dp.message_handler(F.text == "📚 Biologiya DTM Testlar")
async def handle_biology_dtm(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=biology_dtm_dbuttons
    )


@dp.message_handler(F.text == "📌 Yuklab olish PDF (DTM | Biologiya)")
async def handle_biology_dtm_pdf(message: types.Message):
    await send_doc_to_user(message, "dtm_biology")


@dp.message_handler(F.text == "▶️ Test ishlash (DTM | Biologiya)")
async def handle_biology_dtm_play(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )


@dp.message_handler(F.text == "📚 Biologiya Milliy Sertifikat Testlar")
async def handle_biology_sert(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=biology_sert_dbuttons
    )


@dp.message_handler(F.text == "📌 Yuklab olish PDF (Sertifikat | Biologiya)")
async def handle_biology_sert_pdf(message: types.Message):
    await send_doc_to_user(message, "sert_biology")

@dp.message_handler(F.text == "▶️ Test ishlash (Sertifikat | Biologiya)")
async def handle_biology_sert_play(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )
