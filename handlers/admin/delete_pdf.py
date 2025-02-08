from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters import IsBotAdminFilter
from keyboards.inline.admin import chapters_ibutton, delete_pdf_ibutton
from loader import dp, pdb


@dp.message_handler(IsBotAdminFilter(), F.text == "Test o'chirish")
async def handle_delete_tests(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=message.text, reply_markup=chapters_ibutton()
    )


@dp.callback_query_handler(F.data.startswith("ch:"))
async def handle_chapter_selection(call: types.CallbackQuery):
    await call.answer(cache_time=0)
    await call.message.delete()
    test_name = call.data.split(":")[1]
    all_tests = await pdb.select_files_by_name(test_name)
    print(all_tests)
    for test in all_tests:
        await call.message.answer_document(
            document=test['file_id'], reply_markup=delete_pdf_ibutton(test['id'])
        )


@dp.callback_query_handler(F.data.startswith("del_pdf:"))
async def handle_delete_pdf(call: types.CallbackQuery):
    test_id = int(call.data.split(":")[1])
    await pdb.delete_file_by_id(test_id)
    await call.message.delete()
    await call.message.answer(
        text="Test bazadan o'chirildi!"
    )
