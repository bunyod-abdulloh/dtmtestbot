from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    CALL_WITH_ADMIN = State()
    SEND_MESSAGE_TO_USER = State()
