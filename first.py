def pretiffy(symbol):
    def decor(func):
        def wrapper(arg):
            print(symbol*len(arg))
            func(arg)
            print(symbol*len(arg))
        return wrapper
    return decor

@pretiffy('=')
def print_name(name):
    print(name)

@pretiffy('-')
def print_city(city):
    print(city)
if __name__=='__main__':
    print_city('Jakkaram')
    print_name('Srinu')
