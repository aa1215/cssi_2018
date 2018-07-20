print('Hello this is my file')

def my_func(my_str):
    print(my_str)

my_func('Hello I have been called by my_func')

#prevents from being run when importing into the terminal
#line 10 is a boilerplate in Python
if __name__ == '__main__':
    my_func('I am inside a main hm')
