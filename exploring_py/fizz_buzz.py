""" My implementation of fizzbuzz."""

def fizzbuzz(number):
    for x in range(1,number+1):
        if x% 3 == 0 and x % 5 != 0:
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
