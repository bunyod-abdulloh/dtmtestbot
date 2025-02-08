from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_keyboard(buttons, row_width=1):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    for row in buttons:
        markup.row(*[KeyboardButton(text) for text in row])
    return markup


# Admin asosiy tugmalari
admin_main_buttons = create_keyboard([
    ["Test qo'shish", "Test o'chirish"],
    ["Foydalanuvchilar soni"],
    ["Oddiy post yuborish", "Media group yuborish"],
    ["Bosh sahifa"]
])

chemistry_biology_buttons = create_keyboard([
    ["Kimyo bo'limi", "Biologiya bo'limi"],
    ["Ortga"]
])

add_chemistry_buttons = create_keyboard([
    ["Kimyo DTM (PDF)", "Kimyo (Sertifikat)"],
    ["Kimyo DTM (IMAGE)", "Kimyo (Sertifikat/IMAGE)"],
    ["◀️ Ortga"]
])

add_biology_buttons = create_keyboard([
    ["Biologiya DTM (PDF)", "Biologiya (Sertifikat)"],
    ["Biologiya DTN (IMAGE)", "Biologiya (Sertifikat/IMAGE)"],
    ["◀️ Ortga"]
])
