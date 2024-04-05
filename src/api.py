import requests


class HeadHunterAPI:
    @staticmethod
    def get_vacancies(user_input: str) -> dict:
        """ Получение вакансий с hh.ru в формате JSON. """
        url = 'https://api.hh.ru/vacancies'
        params = {'text': user_input, 'search_field': 'name', 'per_page': 100}
        response = requests.get(url, params=params)
        return response.json()['items']
