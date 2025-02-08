from aiogram import types
from magic_filter import F

from keyboards.default.user_dbuttons import user_main_dbuttons
from loader import dp


@dp.message_handler(F.text == "🔙 Ortga")
async def handle_back_user_main(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=user_main_dbuttons
    )

