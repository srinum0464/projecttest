class ValueError(Exception):
    def __init__(self,args):
        self.me = args
if __name__ == '__main__':
    age = 17
    try:
        if age < 18:
            raise ValueError('Your not eligible to register vote minimum age is 18, you age is : {}'.format(age))
        else:
            print('You are eligible to register for vate')
    except ValueError as e:
            print(e)
