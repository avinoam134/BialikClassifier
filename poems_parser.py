import json
from trankit import Pipeline


POEMS_PATH = "./Poems/Poems_Unparsed.JSON"



def load_poems(file_path = POEMS_PATH):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def unload_single_poem(proccesed_poem, file_path):
    with open(file_path, "w") as file:
        json.dump(proccesed_poem, file, indent=4, ensure_ascii=False)


def analyse_single_poem(trankit_pipe, poem_data):
    output_path = f"./Poems/{poem_data['name']}.JSON"
    poem_analysis = trankit_pipe(poem_data["content"])
    unload_single_poem(poem_analysis, output_path)

def analyse_all_poems(trankit_pipe):
    poems = load_poems()
    for poem in poems:
        analyse_single_poem(trankit_pipe, poem)

'''
use this to analyse all poems:

p = Pipeline('hebrew')
analyse_all_poems(p)

'''





