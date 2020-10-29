import os
import pickle

class Files:
    def __init__(self):
        self.__path = os.path.dirname(__file__) + '/data/bangla.pkl'
        self.data = self.__get_files()

    def __get_files(self):
        return pickle.load(open(self.__path, mode='rb'), encoding='utf-8')
    
    def __add_data(self, data):
        pickle.dump(data, open(self.__path, mode='wb'))
        
    def add_data(self, d_type, data):
        """
        Parameters
        ----------
        d_type : str
            'stop_words', 'punctuation', 'letters', 'numbers', 'words', 'words_dict'.
        data : str or list of words

        Returns
        -------
        None.

        """
        try:
            if not isinstance(d_type, str): raise KeyError
            if type(data) not in (str, list): raise Exception('KeyError: Use str or list as parametrs!')
        except KeyError:
            print('KeyError: Use str as paramters!')
        else:
            __data = self.__get_files()
            if isinstance(data, str):
                if d_type == 'words_dict':
                    if data not in __data[d_type][data[0]]: 
                        __data[d_type][data[0]].append(data)
                        print(f'{data} added successfully to {d_type}!')
                    else: print(f'{data} already exist in {d_type}!')
                else:
                    if data in __data[d_type]: 
                        __data[d_type].append(data)
                        print(f'{data} added successfully to {d_type}!')
                    else: print(f'{data} already exist in {d_type}!')
            elif isinstance(data, list):
                if d_type == 'words_dict':
                    error = 0
                    for datum in data:
                        if datum not in __data[d_type][datum[0]]: __data[d_type][datum[0]].append(datum)
                        else: 
                            error+=1
                            print(f'{datum} already exist in {d_type}!')
                            continue
                    print(f'{len(data) - error} data added successfully!')
                    print(f'{error} failed!')
                else:
                    error = 0
                    for datum in data:
                        if datum not in __data[d_type]: __data[d_type].append(datum)
                        else: 
                            error+=1
                            print(f'{datum} already exist in {d_type}!')
                            continue
                    print(f'{len(data) - error} data added successfully!')
                    print(f'{error} failed!')
            self.__add_data(__data)

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
    words = Words()
    get_words = words.get_words(num_of_words = 5, prop="ঐ")
    print(list(get_words))
    for i in get_words:
        print(str(i))
    print(words.STOP_WORDS)
    print(words.PUNCTUATION)
    print(words.LETTERS)
    print(words.NUMBERS)
    
    files = Files()
    files.add_data('words_dict', 'এ')
