from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.admins import IsBotAdminFilter
from handlers.admin.admin_page_main import WARNING_TEXT

from loader import dp, db
from states.admin import AdminStates
from utils.db_functions import send_message_to_users, send_media_group_to_users


@dp.message_handler(IsBotAdminFilter(), F.text == "Oddiy post yuborish", state="*")
async def send_to_bot_users(message: types.Message, state: FSMContext):
    await state.finish()
    send_status = await db.get_send_status()
    if send_status is True:
        await message.answer("Xabar yuborish jarayoni yoqilgan! Hisobot kelganidan so'ng xabar yuborishingiz mumkin!")
    else:
        await message.answer(text=WARNING_TEXT)
        await AdminStates.SEND_TO_USERS.set()


@dp.message_handler(state=AdminStates.SEND_TO_USERS, content_types=types.ContentTypes.ANY)
async def send_to_bot_users_two(message: types.Message, state: FSMContext):
    await state.finish()
    success_count, failed_count = await send_message_to_users(message)

    await db.update_send_status(False)
    await message.answer(
        f"Xabar {success_count} ta foydalanuvchiga yuborildi!\n{failed_count} ta foydalanuvchi botni bloklagan."
    )


@dp.message_handler(IsBotAdminFilter(), F.text == "Media group yuborish", state="*")
async def send_media_to_bot(message: types.Message, state: FSMContext):
    print(message.text)
    await state.finish()
    send_status = await db.get_send_status()
    if send_status is True:
        await message.answer("Xabar yuborish jaroyini yoqilgan! Hisobot kelganidan so'ng xabar yuborishingiz mumkin!")
    else:
        await message.answer(text=WARNING_TEXT)
        await AdminStates.SEND_MEDIA_TO_USERS.set()


@dp.message_handler(state=AdminStates.SEND_MEDIA_TO_USERS, content_types=types.ContentTypes.ANY, is_media_group=True)
async def send_media_to_bot_second(message: types.Message, album: List[types.Message], state: FSMContext):
    await state.finish()
    try:
        media_group = types.MediaGroup()

        for obj in album:
            file_id = obj.photo[-1].file_id if obj.photo else obj[obj.content_type].file_id
            media_group.attach(
                {"media": file_id, "type": obj.content_type, "caption": obj.caption}
            )
    except Exception as err:
        await message.answer(f"Media qo'shishda xatolik!: {err}")
        return

    success_count, failed_count = await send_media_group_to_users(media_group)

    await db.update_send_status(False)
    await message.answer(
        f"Media {success_count} ta foydalanuvchiga yuborildi!\n{failed_count} ta foydalanuvchi botni bloklagan."
    )
