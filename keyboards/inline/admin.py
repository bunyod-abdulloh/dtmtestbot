from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def chapters_ibutton():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Kimyo (DTM | PDF)", callback_data="dtm_chemistry_pdf"),
        InlineKeyboardButton(text="Kimyo (DTM | Image)", callback_data="dtm_chemistry_image"),
        InlineKeyboardButton(text="Kimyo (Sertifikat | PDF)", callback_data="sert_chemistry_pdf"),
        InlineKeyboardButton(text="Kimyo (Sertifikat | Image)", callback_data="sert_chemistry_image"),
        InlineKeyboardButton(text="Biologiya (DTM | PDF", callback_data="dtm_biology_pdf"),
        InlineKeyboardButton(text="Biologiya (DTM | Image)", callback_data="dtm_biology_image"),
        InlineKeyboardButton(text="Biologiya (Sertifikat | PDF)", callback_data="sert_biology_pdf"),
        InlineKeyboardButton(text="Biologiya (Sertifikat | Image)", callback_data="sert_biology_image"),
    )


def delete_pdf_ibutton(id_):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text="O'chirish", callback_data=f"del_pdf:{id_}"))
