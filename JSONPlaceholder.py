import json
import requests


def get_json():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_json = response.json()
    with open("src/response.txt", "w") as f:
        json.dump(todo_json, f, indent=4)
    print(todo_json)


if __name__ == "__main__":
    get_json()
