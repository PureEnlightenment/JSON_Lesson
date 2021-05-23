import json
import requests


def json_reader():
    single_user_get = {}
    with open('src/single_user_get.json') as read_file:
        single_user_get = json.load(read_file)
    print(single_user_get, 'data')  # чтение всего содержимого  вложенного json файла


if __name__ == "__main__":
    json_reader()


def get_and_read_json():
    response = requests.get('https://reqres.in/api/unknown/2')
    online_json = response.content.decode('utf-8')
    print(online_json, 'data')


if __name__ == "__main__":
    get_and_read_json()
