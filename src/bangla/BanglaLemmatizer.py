from .BanglaWords import Words
from .Algorithm import BanglaTrie

class Lemmatizer(BanglaTrie):
    def __init__(self):
        BanglaTrie.__init__(self)

    def get_lemma(self, word_list='default'):
        """
        parameters:
            word_list: take list as argument but by default it takes all words from Words().get_words()
        """
        if word_list != 'default' and not isinstance(word_list, list): raise KeyError('Check word_list type!') 
        self._words_data = Words().get_words() if word_list == 'default' else word_list
        return self._get_lemma()

    # def __stop_words_remove(self):
    #     """
    #     used to remove the stop_words from the Words().STOP_WORDS and 
    #     """
    #     print(self.__stop_words)

    # def __punctuation_remove(self):
    #     """
    #     used to remove the punctuation_word from the Words().PUNCTUATION_LIST
    #     """
    #     print(self.__punctuation_list)

