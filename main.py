from src.api import HeadHunterAPI
from src.config import config
from src.DBM import DBManager


def new_works():
    user_input = 'java'
    params = config()
    # DBManager.create_database(params)
    # DBManager.create_table(params)
    data = HeadHunterAPI.get_vacancies(user_input)
    print(data[0])


if __name__ == '__main__':
    new_works()
