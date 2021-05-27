import json


def another_json_reader():
    data = "src/data_file.json"
    with open(data, 'r') as f:
        data = json.load(f)
        print(data)


if __name__ == "__main__":
    another_json_reader()
