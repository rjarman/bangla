import os
import json

class Files():
    def __init__(self, _data_type, _type, _keys):
        self._path = os.path.dirname(__file__) + '/data/'
        self._type = _type
        self._data_type = _data_type
        self._keys = _keys
    
    def get_data(self):
        data = self.__get_files()
        if self._keys != 'all':
            try:
                return data[self._keys]
            except KeyError:
                print('Error: "check _data_type and _keys!"')
        return data

    def __get_files(self):
        if self._type == 'json': 
            if self._data_type == 'words':
                with open(self._path + 'bangla.json', mode = 'r', encoding = 'utf-8') as file:
                    data = json.loads(file.read())
                return data
            elif self._data_type == 'let_num':
                with open(self._path + 'bangla_letters.json', mode = 'r', encoding = 'utf-8') as file:
                    data = json.loads(file.read())
                return data

if __name__ == '__main__':
    files = Files(_data_type = 'words', _type = 'json', _keys = 'letters')
    print(len(files.get_data()))