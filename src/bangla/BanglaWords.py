from .Generel import Files
class Words(Files):
    def __init__(self, _data_type, _type = 'json', _keys = 'all'):
        Files.__init__(self, _type = _type, _data_type = _data_type, _keys = _keys)

    def get(self):
        return self.get_data()
