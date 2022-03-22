def f(e, t, d=0, u=5):
    pass


print()
print('Hello')
print(5, 'h', True)


q = 50, 45, 67
print(q, type(q))

a, b, c, d = 1, 2, 3, 4


def func(*args):
    print('func')
    print(args)
    print(*args)


func()
func(2, 4, 5)


def func1(*args):
    print('func1')
    # print(args)
    # print(*args)
    func(args)
    func(*args)


func1(7, 8, 9)


def func2(**kwargs):
    print(kwargs)
    # print(**kwargs)


func2(r=6, w=7, y='Hello')
