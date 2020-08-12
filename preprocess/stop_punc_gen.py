import os
import json
import string
import pickle

file_path = os.path.dirname(__file__) + '/'
with open(file_path + 'others.txt', encoding='utf-8') as file:
    ranks = set(file.read().split())
with open(file_path + 'others2.txt', encoding='utf-8') as file:
    kaggle = set(file.read().split())

unique_words = list(ranks.union(kaggle))
punctuation = list(string.punctuation)
punctuation.append('।')

letters = json.load(open(file_path + 'bangla_letters.json', encoding='utf-8'))['letters']
numbers = json.load(open(file_path + 'bangla_letters.json', encoding='utf-8'))['numbers']
words_dict = json.load(open(file_path + 'bangla.json', encoding='utf-8'))
words = []
for i in words_dict:
    for j in words_dict[i]:
        words.append(j)
_dict = {
            "stop_words": unique_words, 
            "punctuation": punctuation,
            "letters": letters,
            "numbers": numbers,
            "words": words,
            "words_dict": words_dict
        }
pickle.dump(_dict, open(file_path + 'bangla.pkl', 'wb'))
# print(pickle.load(open(file_path + 'bangla.pkl', 'rb'), encoding='utf-8')['punctuation'])

