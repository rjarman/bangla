from ..BanglaWords import Words
from .Wrappers import check_lemma, check_insert, check_search

class CharNode:
    def __init__(self):
        self.char_dict = {}
        self.is_end = False

class BanglaTrie:
    def __init__(self):
        self.__char_node = CharNode()
        self.__prefix_stack = []
        self.__populate_words()
        self.__prefix_word = ''

    def __populate_words(self):
        """
        __populate_words is used for populate the dict with bangla words
        """
        words = Words()
        self.insert(list(words.get_words()))

    def __backtrack(self, temp_char_node):
        if temp_char_node.is_end:
            yield self.__prefix_word + ''.join(self.__prefix_stack)
        for _key, char_node in temp_char_node.char_dict.items():
            self.__prefix_stack.append(_key)
            yield from self.__backtrack(char_node)
            self.__prefix_stack.pop()
    
    @check_lemma
    def chk_lemma(self, word):
        """
        parameters:
            word: str of bangla word
        return:
            (str) lemma word
        """
        temp_char_node = self.__char_node
        if word[0] not in temp_char_node.char_dict: return None
        
        make_word = []
        for i in word:
            if i not in temp_char_node.char_dict: return ''.join(make_word)
            make_word.append(i)
            temp_char_node = temp_char_node.char_dict[i]
        join_list = ''.join(make_word)
        return join_list

    @check_insert
    def insert(self, word):
        """
        parameters:
            word: str or list of words
        return:
            (bool) True if words are inserted successfully otherwise False
        """
        try:
            temp_char_node = self.__char_node
            for i in word:
                if i not in temp_char_node.char_dict: temp_char_node.char_dict[i] = CharNode() 
                temp_char_node = temp_char_node.char_dict[i]
            temp_char_node.is_end = True
        except:
            return False
        else:
            return True        

    @check_search
    def search_word(self, word):
        """
        parameters:
            word: str or list of words
        return:
            (iterator) True if words are found successfully otherwise False
        """
        temp_char_node = self.__char_node
        if word[0] not in temp_char_node.char_dict: return False

        for i in word:
            if i not in temp_char_node.char_dict: return False
            temp_char_node = temp_char_node.char_dict[i]
        return True

    def get_prefix_words(self, word):
        """
        parameters:
            word: (str) prefix
        return:
            (iterator) iterator of words depending on prefix
        """
        try:
            if not isinstance(word, str): raise KeyError
        except KeyError:
            print('KeyError: Use str as paramters!')
        else:
            temp_char_node = self.__char_node
            if word[0] not in temp_char_node.char_dict: return False

            for i in word:
                if i not in temp_char_node.char_dict: return False
                temp_char_node = temp_char_node.char_dict[i]
            # if temp_char_node.is_end == True: yield word
            self.__prefix_word = word
            yield from self.__backtrack(temp_char_node)

# test
if __name__ == '__main__':
    banglaTrie = BanglaTrie()
    print(banglaTrie.insert(['saa', 'aaa', 'aasa']))
    print(banglaTrie.insert('umme'))
    print(banglaTrie.insert('umma'))
    print(banglaTrie.insert('ummi'))
    print(banglaTrie.insert('umbrella'))
    banglaTrie.insert('gfg')
    banglaTrie.insert('awe')

    print('\n\nsearching for g: \n', list(banglaTrie.get_prefix_words('um')), '\n\nsearching end')
    print(list(banglaTrie.search_word('aaa')))
    print(list(banglaTrie.search_word(['aaa', 'asa'])))
    print('searching for lemma: ', banglaTrie.chk_lemma('মামাকে'))
    banglaTrie.chk_lemma({'rafsun': 12})
    print(list(banglaTrie.get_prefix_words('মা')))