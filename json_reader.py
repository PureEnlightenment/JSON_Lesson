import json


def json_read():
    users = {}
    with open('src/users.json') as f:  # разобрать что за with и как работает open и что за as и f
        users = json.load(f)
    print("username: " + users['username'])
    print("password: " + users['password'])

    users['password'] = 'helloMoto'
    with open('users.json', 'w') as f:
        json.dump(users, f)  # что за json.dump
    print("New password is: " + users['password'])


if __name__ == '__main__':
    json_read()
