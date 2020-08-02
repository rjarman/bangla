"""
    this module is used to extract and preprocess from the raw data
    N.B. but some preprocessing are done manually
"""

import os
import json
data_path = os.path.dirname(__file__) + '/../src/bangla/data/'

def get_word_list():
    with open(data_path + 'words.txt', 'r', encoding='utf-8') as file:
        words_list = file.read().split('\n')
    return [i for i in words_list if i != '']

def get_letters():
    with open(data_path + 'bangla_letters.json', mode='r', encoding='utf-8') as file:
        letters = json.loads(file.read())
    return letters["letters"]

def get_numbers():
    with open(data_path + 'bangla_letters.json', mode='r', encoding='utf-8') as file:
        letters = json.loads(file.read())
    return letters["numbers"]

def descriminate(letter, word_list = get_word_list()):
    return list(set([i for i in word_list if i[0] == letter]))

"""
print([i for i in get_word_list() if i[0] == '-'])
temp_word_list = [i for i in get_word_list() if ' ' in i]
temp_word_dict = {}
for i in get_letters():
    temp = [i for i in descriminate(i, temp_word_list) if len(i.split()) > 1]
    temp_word_dict.update({i: temp})
json.dump(temp_word_dict, open(data_path + 'temp_bangla.json', mode='w', encoding='utf-8'), ensure_ascii = False)
"""


word_dict = {}
for i in get_letters():
    descriminate_val = descriminate(i)
    if len(descriminate_val) > 0: word_dict.update({i: descriminate_val})
    else: word_dict.update({i: i})
for i in get_numbers():
    word_dict.update({i: i})

json.dump(word_dict, open(data_path + 'bangla.json', mode='w', encoding='utf-8'), ensure_ascii = False)