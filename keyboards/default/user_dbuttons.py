from keyboards.default.admin_buttons import create_keyboard

user_main_dbuttons = create_keyboard(
    [['📚 Kimyo DTM Testlar', '📚 Kimyo Milliy Sertifikat Testlar'],
     ['📚 Biologiya DTM Testlar', '📚 Biologiya Milliy Sertifikat Testlar'],
     ['📲 Adminga murojaat']]
)

chemistry_dtm_dbuttons = create_keyboard([
    ['📌 Yuklab olish PDF (DTM | Kimyo)'],
    ['▶️ Test ishlash (DTM | Kimyo)'],
    ['🔙 Ortga']
])

chemistry_sert_dbuttons = create_keyboard([
    ['📌 Yuklab olish PDF (Sertifikat | Kimyo)'],
    ['▶️ Test ishlash (Sertifikat | Kimyo)'],
    ['🔙 Ortga']
])

biology_dtm_dbuttons = create_keyboard([
    ['📌 Yuklab olish PDF (DTM | Biologiya)'],
    ['▶️ Test ishlash (DTM | Biologiya)'],
    ['🔙 Ortga']
])

biology_sert_dbuttons = create_keyboard([
    ['📌 Yuklab olish PDF (Sertifikat | Biologiya)'],
    ['▶️ Test ishlash (Sertifikat | Biologiya)'],
    ['🔙 Ortga']
])
