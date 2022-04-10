class Mine:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        print('__get_x')
        return self.__x

    @x.setter
    def x(self, x):
        print('__set_x')
        self.__x = x

    @x.deleter
    def x(self):
        print('__del_x')
        self.__x = 0

    @property
    def y(self):
        print('__get_y')
        return self.__y

    @y.setter
    def y(self, y):
        print('__set_y')
        self.__y = y

    @y.deleter
    def y(self):
        print('__del_y')
        self.__y = 0


m1 = Mine(4, 6)
# print(m1.get_x())
print(m1.x)
m1.x = 9
print(m1.x)
del m1.x
print(m1.x)
