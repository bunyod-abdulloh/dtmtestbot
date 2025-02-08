from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters import IsBotAdminFilter
from loader import dp, pdb
from states.admin import AdminStates


async def add_document_func(message: types.Message, test_name: str):
    await pdb.add_file(test_name, message.document.file_id)
    await message.reply(text="Fayl qabul qilindi!")


@dp.message_handler(IsBotAdminFilter(), F.text == "Kimyo DTM (PDF)", state="*")
async def handle_add_kimyo_dtm(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="PDF fayllarni yuboring"
    )
    await AdminStates.ADD_PDF_DTM_CHEMISTRY.set()


@dp.message_handler(state=AdminStates.ADD_PDF_DTM_CHEMISTRY, content_types=types.ContentTypes.DOCUMENT)
async def get_pdf_dtm_chemistry(message: types.Message):
    await add_document_func(message, "dtm_chemistry")


@dp.message_handler(IsBotAdminFilter(), F.text == "Kimyo (Sertifikat)", state="*")
async def handle_add_kimyo_sert(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="PDF fayllarni yuboring"
    )
    await AdminStates.ADD_PDF_SERT_CHEMISTRY.set()


@dp.message_handler(state=AdminStates.ADD_PDF_SERT_CHEMISTRY, content_types=types.ContentTypes.DOCUMENT)
async def get_pdf_sert_chemistry(message: types.Message):
    await add_document_func(message, "sert_chemistry")


@dp.message_handler(IsBotAdminFilter(), F.text == "Biologiya DTM (PDF)", state="*")
async def handle_add_biology_dtm(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="PDF fayllarni yuboring"
    )
    await AdminStates.ADD_PDF_DTM_BIOLOGY.set()


@dp.message_handler(state=AdminStates.ADD_PDF_DTM_BIOLOGY, content_types=types.ContentTypes.DOCUMENT)
async def get_pdf_dtm_biology(message: types.Message):
    await add_document_func(message, "dtm_biology")


@dp.message_handler(IsBotAdminFilter(), F.text == "Biologiya (Sertifikat)", state="*")
async def handle_add_biology_sert(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="PDF fayllarni yuboring"
    )
    await AdminStates.ADD_PDF_SERT_BIOLOGY.set()


@dp.message_handler(state=AdminStates.ADD_PDF_SERT_BIOLOGY, content_types=types.ContentTypes.DOCUMENT)
async def get_pdf_sert_biology(message: types.Message):
    await add_document_func(message, "sert_biology")
