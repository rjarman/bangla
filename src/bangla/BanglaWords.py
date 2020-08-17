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
        self.__num_of_words = None
        self.__set_word_pointer = None
        self.__counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__num_of_words - 1:
            self.__counter += 1
            return self.__set_word_pointer[self.__counter]
        else:
            self.__counter = -1
            raise StopIteration

    def get_words(self, num_of_words = None, prop = 'all'):
        """
        parameters:
            num_of_words: (int) number of total words from datasets, default is None
            prop: (str) takes bangla letters to get that specific words list
        returns:
            iterable object of word
        """
        try: 
            self.__set_word_pointer = self.data['words'] if prop == 'all' else self.data['words_dict'][prop]
            self.__num_of_words = self.__len if num_of_words == None else num_of_words
        except KeyError: print('Error: Check your prop!')
        else: return self

    @property
    def STOP_WORDS(self):
        """
        returns: 
            list of all the bangla stop words
        """
        return self.data['stop_words']

    @property
    def PUNCTUATION(self):
        """
        returns: 
            list of all the bangla punctuations
        """
        return self.data['punctuation']

    @property
    def LETTERS(self):
        """
        returns: 
            list of all the bangla letters
        """
        return self.data['letters']

    @property
    def NUMBERS(self):
        """
        returns: 
            list of all the bangla numbers
        """
        return self.data['numbers']

#   test
if __name__ == '__main__':
    files = Words()
    get_words = files.get_words(num_of_words = 5, prop="ঐ")
    print(list(get_words))
    for i in get_words:
        print(str(i))
    print(files.STOP_WORDS)
    print(files.PUNCTUATION)
    print(files.LETTERS)
    print(files.NUMBERS)
