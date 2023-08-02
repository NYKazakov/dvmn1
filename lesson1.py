import requests


def get_weather(location):
    base_url = 'https://wttr.in/'
    payload = {'nTqmM': '', 'lang': 'ru'}
    url = base_url + location
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text + "\n")


if __name__ == '__main__':
    locations = ["Лондон", "Аэропорт", "Череповец"]
    for location in locations:
        get_weather(location)
