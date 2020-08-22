from .BanglaWords import Words
from .lib.Algorithm import BanglaTrie

class Lemmatizer(BanglaTrie):
    def __init__(self):
        BanglaTrie.__init__(self)

    def get_lemma(self, word):
        """
        parameters:
            word: (str or list) takes str or list of words
        return:
            (iterator) str of lemma word
        """
        validation = (str, list)
        if type(word) in validation:
            if isinstance(word, str): yield self.chk_lemma(word)
            else:
                for i in word:
                    if not isinstance(i, str): raise ValueError(f'Use str into the list!')
                    yield self.chk_lemma(i)
        else: 
            raise KeyError(f'Use str or list as paramters!')

