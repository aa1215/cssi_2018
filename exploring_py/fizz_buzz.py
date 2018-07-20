""" My implementation of fizzbuzz."""


"""Prints out fizz, buzz, or fizzbuzz depending on divisibility by 3 and/or 5.

Prints out fizz if a number is only divisible by 3 and not 5.
Prints out buzz if a number is only divisible by 5 and not 3.
Prints out fizzbuzz if a number is divisible by both 3 and 5.

Args:
    number: (int) The maximum integer to check divisibility of numbers up until.
Returns:
    (str) Either fizz, buzz, or fizzbuzz depending on divisibility.
"""

def fizzbuzz(number):
    for x in range(1,number+1):
        if x % 3 == 0 and x % 5 != 0:
            print('fizz')
        elif x % 5 ==0 and x % 3 != 0:
            print('buzz')
        elif x % 3 ==0 and x % 5 == 0:
            print('fizzbuzz')
        else:
            print('none')

num = input('What number would you like to choose?: ')
fizzbuzz(num)

# def fizzbuzz1(num):
#     num1 = input('What number would you like to choose?: ')
#     for x in range(1,num+1):
#         if x% 3 == 0 and x % 5 != 0:
#             return 'fizz'
#         elif x % 5 ==0 and x % 3 != 0:
#             return 'buzz'
#         elif x % 3 ==0 and x % 5 == 0:
#             return 'fizzbuzz'
#         else:
#             return 'none'
# print(fizzbuzz1(9))
