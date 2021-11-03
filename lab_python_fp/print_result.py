def print_result(func):
    def printing(*args):
        if len(args) > 0:
            data = func(args[0])
        else:
            data = func()
        print(func.__name__)
        if type(data) is list:
            for i in data:
                print(i)
        elif type(data) is dict:
            for key, value in data.items():
                print(key, ' = ', value)
        else:
            print(data)
        return data
    return printing
