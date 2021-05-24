import json
import requests


def create_user_json():  # для reqres.in
    user_for_create = {}
    with open('src/user_for_create.json') as p:
        user_for_create = json.load(p)
        payload = user_for_create
    request = requests.post("https://reqres.in/api/users", data=payload)  # отправляем запрос с определенным json
    print(user_for_create)
    print(request.status_code)
    print(request.content)
    # user_for_create['name'] = 'neo'
    # with open("src/user_for_create.json", 'w') as c:
    # json.dump(user_for_create, c)
    # print(request.text)
    # реализовать запись перезапись джейсона,  затем отправку на сервер


if __name__ == "__main__":
    create_user_json()





