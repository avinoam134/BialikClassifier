import json


POEMS_PATH = "./Poems/Poems_Unparsed.JSON"


def parse_poems(file_path = POEMS_PATH):
    with open(file_path, "r") as file:
        data = json.load(file)
    data = [poem["content"] for poem in data]
    return data

    


