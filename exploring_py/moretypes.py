"""More exploratory stuff """


x = [1,2,3,1]
x.append(99)
print(x)

print(len(x))
print(x.pop())
print(x)

x.reverse()
print(x)
print(x.count(1))

print(3 in x)


#sets have all unique values

aksharas_dict = {'name': 'Akshara', 'age': 17, 'interests': ['outdoors', 'travel', 'fitness', 'reading', 'cs'], 'school': 'Duke'}
print(aksharas_dict)

for key in aksharas_dict:
    print('{k}: {v}'.format(k=key,v=aksharas_dict[key]))

for val in aksharas_dict:
    print(val)

print(aksharas_dict.items())

for key, value in aksharas_dict.items():
    print(key + str(value))

for key in aksharas_dict:
    if key == 'name':
        print('I found the key for name!')

#lambda function
my_throwaway = lambda val: val + 1000
def func(a,b):
    return a + b

def foo(ls, func):
    new_ls = []
    for thing in ls:
        new_ls.append(func(thing))
    return new_ls

def add_one(val):
    return val + 1

foo(x,add_one)

#looping through the dictionary as a list of tuples
my_dict = ('name': 'Akshara', 'age': '17')
for thing in my_dict.items():
    x, y = thing
    print('Key: {k}, Value: {v}'.format(k=x, v=y))
