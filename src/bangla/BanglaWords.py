import os
import pickle

class Files:
    def __init__(self):
        self.__path = os.path.dirname(__file__) + '/data/bangla.pkl'
        self.data = self.get_files()

    def get_files(self):
        return pickle.load(open(self.__path, mode='rb'), encoding='utf-8')

class Words(Files):
    def __init__(self):
        Files.__init__(self)

    def get_words(self, prop = 'all'):
        if prop == 'all': return self.data['words']

        try:
            return self.data['words_dict'][prop]
        except KeyError:
            print('Check your keys parameter!')

    @property
    def STOP_WORDS(self):
        return self.data['stop_words']

    @property
    def PUNCTUATION(self):
        return self.data['punctuation']

    @property
    def LETTERS(self):
        return self.data['letters']

    @property
    def NUMBERS(self):
        return self.data['numbers']

if __name__ == '__main__':
    files = Words()
    print(files.get_words('k'))