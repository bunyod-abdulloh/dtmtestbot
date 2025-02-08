from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def send_message_to_admin(user_id):
    """Administratorga foydalanuvchi haqida xabar yuborish tugmasi."""
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text="Javob yuborish", callback_data=f"user_message:{user_id}")
    )
