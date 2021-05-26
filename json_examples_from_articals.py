import json


def serrialization_test():
    data = {  # объявляем json с содержимым
        "president": {
            "name": "Zaphod Beeblebroxx",
            "species": "Betelgeusian"
        }
    }

    with open("src/data_json.json", "w") as write_json:  # зыписываем в пустой json файл наш объявленный выше json
        json.dump(data, write_json)


if __name__ == "__main__":  # запуск функции
    serrialization_test()
