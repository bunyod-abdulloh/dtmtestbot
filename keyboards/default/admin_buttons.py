from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_keyboard(buttons, row_width=1):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    for row in buttons:
        markup.row(*[KeyboardButton(text) for text in row])
    return markup


# Admin asosiy tugmalari
admin_main_buttons = create_keyboard([
    ["Test qo'shish (PDF)", "Test qo'shish (IMAGE)"],
    ["Foydalanuvchilar soni"],
    ["Oddiy xabar yuborish", "Media group yuborish"],
    ["Bosh sahifa"]
])

add_pdf_buttons = create_keyboard([
    ["Kimyo DTM (PDF)", "Kimyo (Sertifikat)"],
    ["Biologiya DTN (PDF)", "Biologiya (Sertifikat)"],
    ["◀️ Ortga"]
])

add_image_buttons = create_keyboard([
    ["Kimyo DTM (IMAGE)", "Kimyo (Sertifikat/IMAGE)"],
    ["Biologiya DTN (IMAGE)", "Biologiya (Sertifikat/IMAGE)"],
    ["◀️ Ortga"]
])