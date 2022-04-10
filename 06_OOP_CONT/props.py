class Mine:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __get_x(self):
        print('__get_x')
        return self.__x

    def __set_x(self, x):
        print('__set_x')
        self.__x = x

    def __del_x(self):
        print('__del_x')
        self.__x = 0

    def __get_y(self):
        print('__get_y')
        return self.__y

    def __set_y(self, y):
        print('__set_y')
        self.__y = y

    def __del_y(self):
        print('__del_y')
        self.__y = 0

    x = property(__get_x, __set_x, __del_x)
    y = property(__get_y, __set_y, __del_y)


m1 = Mine(4, 6)
# print(m1.get_x())
print(m1.x)
m1.x = 9
print(m1.x)
del m1.x
print(m1.x)
