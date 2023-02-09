import re

import requests
import wikipediaapi


def weather_main(url='', query_city='ekaterinburg'):
    """ Использование OpenWeather Api для получения погоды в формате JSON"""
    app_key = ''  # Ключ, получаем после регистрации на openweathermap.org
    params = {'q': query_city, 'units': 'metric', 'lang': 'ru', 'appid': app_key}
    response = requests.get(url=url, params=params)  # Формирование url запроса
    data = response.json()
    return data


def one_days(my_query_city='ekaterinburg'):
    """ Получение информации о погоде на один день"""
    url = 'https://api.openweathermap.org/data/2.5/weather'
    data = weather_main(url=url, query_city=my_query_city)  # получение данных в json формате
    temp_data = f"Температура: {data['main']['temp']} °C"
    sky_data = f"Небо: {data['weather'][0]['description']}"
    pressure_data = f"Давление: {data['main']['pressure']}"
    humidity_data = f"Влажность: {data['main']['humidity']}"
    return f"{temp_data}\n{sky_data}\n{pressure_data}\n{humidity_data}"


def five_days(query_city='ekaterinburg'):
    """ Получение информации о погоде на пять день """
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    data = weather_main(url=url, query_city=query_city)  # получение данных в json формате
    for i in data['list']:
        if [i['dt_txt']][0][11:] == '12:00:00':
            a, b = i['main']['temp'], i['dt_txt']
            d = f'{b}, Температура: {a} C'
            print(d)

    # return f'{d}'
    # print(f'{b}, Температура: {a} C')
    # plt.plot(b, a)
    # plt.show()


def finding_definitions(words: str) -> str:
    """ Поиск определения понятий в википедии """
    wiki = wikipediaapi.Wikipedia(language='ru', extract_format=wikipediaapi.ExtractFormat.WIKI)
    page_py = wiki.page(words)
    text_find = page_py.text
    text = remove_text_between_parens(text_find)
    result = text[:text.find('.')] + '.'  # удаление текста после первой точки
    return result


def remove_text_between_parens(text):
    """ Удаление скобок и их содержимого """
    n = 1
    while n:
        text, n = re.subn(r'\([^()]*\)', '', text)
    return text

#
# print(finding_definitions('саспенс'))
