import asyncio

from aiogram import types
from magic_filter import F

from keyboards.default.user_dbuttons import chemistry_dtm_dbuttons, chemistry_sert_dbuttons
from loader import dp, pdb


async def send_doc_to_user(message: types.Message, test_name: str):
    all_tests = await pdb.select_files_by_name(test_name)
    if not all_tests:
        await message.answer(
            text="Testlar hozircha joylanmadi!"
        )
        return
    for index, test in enumerate(all_tests):
        if index == 29:
            await asyncio.sleep(5)
        await message.answer_document(document=test['file_id'], protect_content=True)


@dp.message_handler(F.text == "📚 Kimyo DTM Testlar")
async def handle_chemistry_dtm(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=chemistry_dtm_dbuttons
    )


@dp.message_handler(F.text == "📌 Yuklab olish PDF (DTM | Kimyo)")
async def handle_chemistry_dtm_pdf(message: types.Message):
    await send_doc_to_user(message, "dtm_chemistry")


@dp.message_handler(F.text == "▶️ Test ishlash (DTM | Kimyo)")
async def handle_chemistry_dtm_play(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )


@dp.message_handler(F.text == "📚 Kimyo Milliy Sertifikat Testlar")
async def handle_chemistry_sert(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=chemistry_sert_dbuttons
    )


@dp.message_handler(F.text == "📌 Yuklab olish PDF (Sertifikat | Kimyo)")
async def handle_chemistry_sert_pdf(message: types.Message):
    await send_doc_to_user(message, "sert_chemistry")


@dp.message_handler(F.text == "▶️ Test ishlash (Sertifikat | Kimyo)")
async def handle_chemistry_sert_play(message: types.Message):
    await message.answer(
        text="Testlar hozircha joylanmadi!"
    )
