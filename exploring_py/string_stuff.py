print("Hello")

def func(asdf):
    print(asdf)

# #how to split a string by spaces
# my_string = "hello i am akshara anand"
# output = my_string.split(' ')
# print(output)
#
# #turning a string into a list and a list back into a string
# #join
# string_1 = 'golden goose granola grains grapes'
# my_list = list(string_1)
# ''.join(my_list)
#
# #turning a list back to a string to a for loop
# for thing in my_list:
#     my_final_string += thing
#
# #some more practice
# x = ['<body>', '<p>', '</body>', '</p>' ]
# my_html_string = '\n'.join(x)
# print(my_html_string)
#
# #LOL!!! this is gonna output something ridiculous bc the list splits up the string into its characters!
# 'banananas'.join(list("this stuff is"))
# #this one's what we
# 'banananas'.join('this stuff is'.split(' '))
#
# dog = 'Cheddar'
# list(dog)
# dog.split('ar')
#
# # \n means new line
# dog = 'Chedd\nar'
# print(dog)
#
#
# #changing the string's spaces into underscores
# par = 'Hi my name is Akshara Anand and I am at Google CSSI'
#
# #simple way to do this
# '_'.join(par.split(' '))
#
# #doing this through a for loop
# new_string = ''
# new_list = list(par)
# for x in new_list:
#     if x == ' ':
#         new_string += '_'
#     else:
#         new_string += x
# print(new_list)
