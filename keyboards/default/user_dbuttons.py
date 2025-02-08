from keyboards.default.admin_buttons import create_keyboard

user_main_dbuttons = create_keyboard(
    [['📚 Kimyo DTM Testlar', '📚 Kimyo Milliy Sertifikat Testlar'],
     ['📚 Biologiya DTM Testlar', '📚 Biologiya Milliy Sertifikat Testlar']]
)

# Testlar hammasi lotinda
chemistry_dtm_dbuttons = create_keyboard([
    ['📌 Testlar varianti (PDF)'],
    ['▶️ Test ishlash (Kimyo DTM)'],
    ['🔙 Ortga']
])

# Testlar e kirillda
chemistry_sert_dbuttons = create_keyboard([
    ['📌 Tеstlar varianti (PDF)'],
    ['▶️ Test ishlash (Kimyo Milliy Sertifikat)'],
    ['🔙 Ortga']
])

# Testlar e kirill a kirillda
biology_dtm_dbuttons = create_keyboard([
    ['📌 Tеstlаr varianti (PDF)'],
    ['▶️ Test ishlash (Biologiya DTM)'],
    ['🔙 Ortga']
])

# Testlar e lotin a kirillda
biology_sert_dbuttons = create_keyboard([
    ['📌 Tеstlar varianti (PDF)'],
    ['▶️ Test ishlash (Biologiya DTM)'],
    ['🔙 Ortga']
])
