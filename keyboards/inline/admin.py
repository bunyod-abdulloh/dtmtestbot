from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def chapters_ibutton():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Kimyo (DTM | PDF)", callback_data="ch:dtm_chemistry"),
        InlineKeyboardButton(text="Kimyo (DTM | Image)", callback_data="test:dtm_chemistry_img"),
        InlineKeyboardButton(text="Kimyo (Sertifikat | PDF)", callback_data="ch:sert_chemistry"),
        InlineKeyboardButton(text="Kimyo (Sertifikat | Image)", callback_data="test:sert_chemistry_img"),
        InlineKeyboardButton(text="Biologiya (DTM | PDF)", callback_data="ch:dtm_biology"),
        InlineKeyboardButton(text="Biologiya (DTM | Image)", callback_data="test:dtm_biology_img"),
        InlineKeyboardButton(text="Biologiya (Sertifikat | PDF)", callback_data="ch:sert_biology"),
        InlineKeyboardButton(text="Biologiya (Sertifikat | Image)", callback_data="test:sert_biology_img")
    )
    return markup


def delete_pdf_ibutton(id_):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text="O'chirish", callback_data=f"del_pdf:{id_}"))
    return markup
