import json


def json_reader():
    single_user_get = {}
    with open('src/single_user_get.json') as read_file:
        single_user_get = json.load(read_file)
    print(single_user_get, 'data')  # чтение всего содержимого  вложенного json файла


if __name__ == "__main__":
    json_reader()
