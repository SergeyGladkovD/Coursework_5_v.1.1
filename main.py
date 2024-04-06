from src.api import HeadHunterAPI
from src.config import config
from src.dbm import DBManager


def new_works():
    while True:
        user_input = input(f'Хотите посмотреть созданную таблицу вакансий нажмите 1\n'
                           f'Хотите удалит созданную таблицу и начать новый поиск вакансий нажмите 2\n'
                           f'Остальные команды прекратят работу программы.\n')
        if user_input == '1':
            print("Тут надо прописать логику и запуск bdm команд.")
            break
        elif user_input == '2':
            params = config()
            DBManager.create_database(params)
            DBManager.create_table(params)
            vacancy = input('Какую вакансию вы ищете?\n')
            city = input('В каком городе?\n')
            data = HeadHunterAPI.get_vacancies(vacancy, city)
            DBManager.add_data_in_bd(data, params)

        else:
            print('Программа завершена.')
        break


if __name__ == '__main__':
    new_works()
