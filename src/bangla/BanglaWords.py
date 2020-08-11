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
        self.__len = len(self.data['words'])

    def get_words(self, num_of_words = None, prop = 'all'):
        """
        parameters:
            num_of_words: (int) number of total words from datasets, default is None
            prop: (str) takes bangla letters to get that specific words list
        """
        if prop == 'all':
            num_of_words = self.__len if num_of_words == None else num_of_words
            yield from self.__pull_words(num_of_words = num_of_words)
        else:
            yield from self.__pull_words(num_of_words = num_of_words, keys=prop)

    def __pull_words(self, num_of_words, keys = None):
        """
        parameters:
            num_of_words: (int) number of total words from datasets, default is None
            prop: (str) takes bangla letters to get that specific words list
        """
        __len_counter = 0
        try: __data = self.data['words'][__len_counter] if keys == None else self.data['words_dict'][keys][__len_counter]
        except KeyError: print('Error: Check your prop!')
        else:
            while __len_counter < num_of_words:
                yield __data
                __len_counter += 1

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

#   test
if __name__ == '__main__':
    files = Words()
    a = files.get_words(num_of_words = 10, prop='2')
    # a.__next__()
    # print(list(a))
    for i in a:
        print(str(i))