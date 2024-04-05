import psycopg2


class DBManager:

    @staticmethod
    def create_database(params: dict, database_name='new_works'):
        """ Создает базу данных. """
        conn = psycopg2.connect(dbname='postgres', **params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f'DROP DATABASE IF EXISTS {database_name}')
        cur.execute(f'CREATE DATABASE {database_name}')
        conn.close()

    @staticmethod
    def create_table(params: dict, database_name='new_works'):
        """ Создает таблицу. """
        conn = psycopg2.connect(dbname=database_name, **params)
        with conn.cursor()as cur:
            cur.execute("""
            CREATE TABLE employers (
                channel_id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                views INTEGER,
                subscribers INTEGER,
                videos INTEGER,
                channel_url TEXT
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def get_companies_and_vacancies_count():
        """ Получает список всех компаний и количество вакансий у каждой компании. """
        pass

    @staticmethod
    def get_all_vacancies():
        """  Получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию. """
        pass

    @staticmethod
    def get_avg_salary():
        """  Получает среднюю зарплату по вакансиям. """
        pass

    @staticmethod
    def get_vacancies_with_higher_salary():
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. """
        pass

    @staticmethod
    def get_vacancies_with_keyword():
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python. """
        pass
