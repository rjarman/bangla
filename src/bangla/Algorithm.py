class CharNode:
    def __init__(self, char_num):
        self.__char_node = [None] * char_num
        self.__is_end = False

class BanglaTrie:
    def __init__(self):
        self.__words = []

    def insert(self, word):
        pass

    def search_word(self, word):
        pass

    def delete(self, word):
        pass
    

    def _get_lemma(self):
        
        print(len(self.__words))

    @property
    def _words_data(self):
        return self.__words
    @_words_data.setter
    def _words_data(self, words):
        self.__words = words


class PreSearch(BanglaTrie):
    def __init__(self):
        PreSearch.__init__(self)
    
    def get_prefix_list(self, word):
        pass
if __name__ == '__main__':

    banglaTrie = BanglaTrie()
    # banglaTrie.__words_data = 'abav'
    # print(banglaTrie.__words_data)
    print(banglaTrie._get_lemma())