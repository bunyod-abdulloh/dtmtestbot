from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStates(StatesGroup):
    SEND_MEDIA_TO_USERS = State()
    SEND_TO_USERS = State()
    SEND_POST_TO_GROUP = State()
    SEND_MEDIA_TO_GROUP = State()
    SEND_POST_TO_GROUPS = State()
    SEND_MEDIA_TO_GROUPS = State()
    ADD_BOT_TO_GROUP = State()
    ADD_REFERRAL = State()
    ADD_PDF_DTM_CHEMISTRY = State()
    ADD_PDF_SERT_CHEMISTRY = State()
    ADD_PDF_DTM_BIOLOGY = State()
    ADD_PDF_SERT_BIOLOGY = State()
    ADD_IMAGE = State()
