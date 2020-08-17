def check_lemma(function):
    def wrapper(*args):
        try:
            if not isinstance(args[1], str):
                raise KeyError
        except KeyError:
            print('KeyError: Use str as paramters!')
        else:
            return function(*args)
    return wrapper

def check_insert(function):
    validation = (str, list)
    def wrapper(*args):
        if type(args[1]) in validation:
            if isinstance(args[1], str):
                if not function(*args): raise Exception(f'{args[1]} insertion failed!')
                return True
            else:
                for i in args[1]:
                    if not isinstance(i, str): raise ValueError(f'Use str into the list!')
                    if not function(*(args[0], i)): raise Exception(f'{i} insertion failed!')
                return True
        else:
            raise KeyError(f'Use str or list as paramters!')
    return wrapper

def check_search(function):
    validation = (str, list)
    def wrapper(*args):
        if type(args[1]) in validation:
            if type(args[1]) == validation[0]:
                yield function(*args)
            if type(args[1]) == validation[1]:
                for i in args[1]:
                    if not isinstance(i, str): raise ValueError(f'Use str into the list!')
                    yield function(*(args[0], i))
        else:
            raise KeyError(f'Use str or list as paramters!')
    return wrapper