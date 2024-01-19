import json

POEMS_PATH = "./Poems/Poems_Unparsed.JSON"

def parse_poems(file_path = POEMS_PATH, encoding='utf-8'):
    with open(file_path, "r", encoding=encoding) as file:
        data = json.load(file)
    return data

data = parse_poems(POEMS_PATH)
print(data)


