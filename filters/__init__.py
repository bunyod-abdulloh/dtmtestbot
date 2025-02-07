from loader import dp
from .admins import AdminFilter, IsBotAdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsBotAdminFilter)
