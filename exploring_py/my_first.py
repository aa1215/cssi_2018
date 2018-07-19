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
