"""
class ClassName:
    class_body

class ClassName(ParentClass1, ParentClass2):
    class_body
"""


class Point:
    # x = 0
    # y = 0
    name = 'Test'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x


pt1 = Point(5, 7)
print(dir(pt1))
# pt1.x = 8
# print(pt1.x)
# pt1.set_x(9)
print(pt1.x)
pt2 = Point(4, 8)
pt3 = Point(9, 2)
print(pt2.x)
print(pt3.x)
print(pt1.name)
print(pt2.name)
print(pt3.name)
Point.name = 'Test1'
print(pt1.x)
print(pt2.x)
print(pt3.x)
print(pt1.name)
print(pt2.name)
print(pt3.name)
pt2.name = 'Some string'
print(pt1.name)
print(pt2.name)
print(pt3.name)


class Triangle:
    def __init__(self, pic1, pic2, pic3):
        self.pic1 = pic1
        self.pic2 = pic2
        self.pic3 = pic3


tr = Triangle(pt1, pt2, pt3)

print(tr.pic2.y)


class SomeClass:
    pass


print(dir(SomeClass))


def square_method(self):
    return self.x ** 2


def init(self, x):
    self.x = x


SomeClass.new_attr = 56
SomeClass.init = init
SomeClass.square = square_method
sc = SomeClass()
print(dir(sc))
sc.init(23)
print(sc.square())


class StaticMethodClass:
    @staticmethod
    def func():
        print('Static method')


smc = StaticMethodClass()
smc.func()
StaticMethodClass.func()


class ClassMethod:
    @classmethod
    def func1(cls):
        print('Class method')


class Person:
    def __new__(cls, *args, **kwargs):
        print('Constructor')
        return super().__new__(cls)

    def __init__(self, x):
        self.x = x
        print('Init')

    def __del__(self):
        print('Destructor')

    def __str__(self):
        return f'To string. Attribute X = {self.x}'

    def __repr__(self):
        return str(self.x)


p = Person(5)
# del p
print(str(p))
