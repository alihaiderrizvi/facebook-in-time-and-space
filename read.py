import json

def read(path):
    with open(path) as file:
        data = json.load(file)

    return data
