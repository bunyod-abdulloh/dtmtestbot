from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from magic_filter import F

from filters.admins import IsBotAdminFilter
from keyboards.default.admin_buttons import admin_main_buttons, chemistry_biology_buttons
from loader import dp, db

# Xabarlar va ogohlantirish matni
WARNING_TEXT = (
    "Xabar yuborishdan oldin postingizni yaxshilab tekshirib oling!\n\n"
    "Imkoni bo'lsa postingizni oldin tayyorlab olib keyin yuboring.\n\n"
    "Xabaringizni kiriting:"
)


@dp.message_handler(IsBotAdminFilter(), Command(commands="admin"))
async def admin_main_page(message: types.Message):
    await message.answer("Admin panel", reply_markup=admin_main_buttons)


@dp.message_handler(IsBotAdminFilter(), F.text == "Ortga")
async def back_to_main_page(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Admin bosh sahifasi!", reply_markup=admin_main_buttons)

@dp.message_handler(IsBotAdminFilter(), F.text == "◀️ Ortga", state="*")
async def back_to_chemistry_biology(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=message.text, reply_markup=chemistry_biology_buttons)



@dp.message_handler(IsBotAdminFilter(), F.text == "Foydalanuvchilar soni")
async def show_user_count(message: types.Message, state: FSMContext):
    await state.finish()
    user_count = await db.count_users()
    await message.answer(f"Foydalanuvchilar soni: {user_count}")


@dp.message_handler(IsBotAdminFilter(), F.text == "Test qo'shish")
async def handle_add_pdf(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="Test qo'shiladigan bo'limni tanlang", reply_markup=chemistry_biology_buttons
    )
