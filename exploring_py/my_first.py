"""This is my file - Akshara Anand

This is the first python file I'm writing for CSSI.
"""

# print('Hello World')
#
# x = 5
# if x > 3:
#     print("You got this")
# else:
#     print("ok let's try again")
#
# x = 1
# while x <= 5:
#     print(x)
#     x+=1
#
list = ['apple', 'banana', 'carrot']

for x in list:
    print(x)

for x in range(5):
    print(x)

for thing in "hello":
    print(thing)

# for val in range(15,100):
#     print('{val} is divisible by 2: {dunno}'.format(
#         val=val, dunno=val%2 == 0))

def isThisOk(x):
    print(x%2)

isThisOk(4)

def nextOne(x):
    return x - 2

print(nextOne(4))

# below is pep 257
"""Prints out a person's name.

This function prints out a person's name. Nothing special.

Args:
    first: (str) The person's first name
    last_name: (str) The person's last name
    middle_name: (str) Optional. The person's middle name
Returns:
    (str) The string of the person's name.
"""
def print_person(first, last_name, middle_name=None):
    middle_name = middle_name or ''
    print('{f} {m} {l}'.format(f=first,m=middle_name,l=last_name))
