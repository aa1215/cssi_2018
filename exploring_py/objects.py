class Person(object):
    #you have to pass in self
    def __init__(self, name, age, school, phone):
        #defining attributes
        self.name = name
        self.age = age
        self.school = school
        self.phone = phone
        self.hungry = True
        self.work = False

    def eat(self, food):
        print('I am eating {food}'.format(food=food))
        self.hungry = False

    def workout(self, ty, time):
        print('My workout was {w} and I did it for {m} minutes'.format(w=ty, m=time))
        self.workout = True

akshara = Person(name='Akshara', age=17, school='Duke', phone='iPhone X')
bob = Person(name='Bob', age=19, school='UT Austin', phone='Android')
cheddar = Person(name='Cheddar', age=5, school='Dog Academy', phone='iCorgi')
akshara.eat('quinoa')
akshara.workout('a run', 60)

print(akshara.name)
print(akshara.hungry)








class Course(object):
    def __init__(self, area, level, available):
        self.area = area
        self.level = level
        self.available = available

linear_alg = Course(area='math', level=5, available = True)
greek = Course(area='fl', level=3, available = False)

print(greek.available)
print(linear_alg.level)
