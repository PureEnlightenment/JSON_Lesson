import json


def json_changer():
    test_json = {}  # объявляем пустой json
    # обортываем в with и указываем через
    # open из какого файла хотим загрузить json
    with open('src/test_json.json') as f:
        test_json = json.load(f)  # загружаем json

        test_json['name'] = "python guru"  # меняем значение ключа name
        # обертываем в with и указываем путь и  'w', для изменения json
        with open('src/test_json.json', 'w') as w:
            json.dump(test_json, w)  # изменяем json
    print(test_json['name'])  # печатаем название нового ключа - вуаля!


if __name__ == "__main__":
    json_changer()
