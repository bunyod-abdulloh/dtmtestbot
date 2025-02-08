from aiogram import types
from magic_filter import F

from loader import dp, pdb


@dp.callback_query_handler(F.data.starstwith("del_pdf:"))
async def delete_pdf_callback(call: types.CallbackQuery):
    id_ = int(call.data.split(":")[1])
    all_tests = await pdb.get_all_files()

    for test in all_tests:


