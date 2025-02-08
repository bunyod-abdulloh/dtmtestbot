from keyboards.default.user_dbuttons import user_main_dbuttons

from aiogram import types
from magic_filter import F

from data.config import CHANNELS

from loader import bot, dp


async def not_subcribe_message(call: types.CallbackQuery):
    await call.answer(
        text=f"Ikkala kanalga ham a'zo bo'lishingiz lozim!", show_alert=True
    )


@dp.callback_query_handler(F.data == "subscribed")
async def subscribe_callback(call: types.CallbackQuery):
    first_channel = (await bot.get_chat_member(chat_id=CHANNELS[0], user_id=call.from_user.id)).status
    second_channel = (await bot.get_chat_member(chat_id=CHANNELS[1], user_id=call.from_user.id)).status

    if first_channel == 'left' or second_channel == 'left':
        await not_subcribe_message(call=call)
    elif first_channel == 'kicked' or second_channel == 'kicked':
        await not_subcribe_message(call=call)
    else:
        await call.message.delete()
        await call.message.answer(
            text="Assalomu alaykum! Botimizga xush kelibsiz!", reply_markup=user_main_dbuttons
        )
