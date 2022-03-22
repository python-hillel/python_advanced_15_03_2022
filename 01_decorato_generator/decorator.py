# def measure_time(function):
#     from datetime import datetime
#
#     def wrapper():
#         start = datetime.now()
#         result = function()
#         print(datetime.now() - start)
#         return result
#     return wrapper
#
#
# @measure_time
# def gen():
#     """
#     Генератор списков
#     :return: List
#     """
#     lst = []
#     for i in range(10 ** 5):
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
#
# print('Name:', gen.__name__)
# print('Doc:', gen.__doc__)
#
#
# def measure_time1(function):
#     from datetime import datetime
#
#     def wrapper():
#         start = datetime.now()
#         result = function()
#         print(datetime.now() - start)
#         return result
#
#     wrapper.__name__ = function.__name__
#     wrapper.__doc__ = function.__doc__
#
#     return wrapper
#
#
# @measure_time1
# def gen():
#     """
#     Генератор списков
#     :return: List
#     """
#     lst = []
#     for i in range(10 ** 5):
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
#
# print('Name:', gen.__name__)
# print('Doc:', gen.__doc__)


# from functools import update_wrapper
#
#
# def measure_time(function):
#     from datetime import datetime
#
#     def wrapper():
#         start = datetime.now()
#         result = function()
#         print(datetime.now() - start)
#         return result
#
#     update_wrapper(wrapper, function)
#
#     return wrapper
#
#
# @measure_time
# def gen():
#     """
#     Генератор списков
#     :return: List
#     """
#     lst = []
#     for i in range(10 ** 5):
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
#
# print('Name:', gen.__name__)
# print('Doc:', gen.__doc__)


# from functools import wraps
#
#
# def measure_time(function):
#     from datetime import datetime
#
#     @wraps(function)
#     def wrapper():
#         start = datetime.now()
#         result = function()
#         print(datetime.now() - start)
#         return result
#
#     return wrapper
#
#
# @measure_time
# def gen():
#     """
#     Генератор списков
#     :return: List
#     """
#     lst = []
#     for i in range(10 ** 5):
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
#
# print('Name:', gen.__name__)
# print('Doc:', gen.__doc__)


# from functools import wraps
#
#
# def measure_time(function):
#     from datetime import datetime
#
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         result = function(*args, **kwargs)
#         print(datetime.now() - start)
#         return result
#
#     return wrapper
#
#
# @measure_time
# def gen(cnt):
#     """
#     Генератор списков
#     :return: List
#     """
#     lst = []
#     for i in range(cnt):
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
#
# print(len(gen(10 ** 6)))


# def pre(cond, msg):
#     from functools import wraps
#
#     def outer(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             assert cond(*args, **kwargs), msg
#             return func(*args, **kwargs)
#         return inner
#     return outer
#
#
# @pre(lambda a: a >= 0, 'Negative argument')
# def check_log(x):
#     print('check_log - RUN')
#     from math import log
#     return log(x)
#
#
# print(check_log(45))        # 3.8066624897703196
# print(check_log(-5))        # AssertionError: Negative argument


# import math
#
#
# def post(cond, msg):
#     from functools import wraps
#
#     def wrapper(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             res = func(*args, **kwargs)
#             assert cond(res), msg
#             return res
#         return inner
#     return wrapper
#
#
# @post(lambda x: not math.isnan(x), 'Not A Number')
# def something_useful(param=None):
#     if param is None:
#         return float('nan')
#     else:
#         return float(param)
#
#
# print(something_useful('4.56'))             # 4.56
# print(something_useful())                   # AssertionError: Not A Number

def decor1(func):
    return lambda x: func(x * x)


def decor2(func):
    return lambda x: func(x + 42)


@decor1
@decor2
def identity1(a):
    return a


@decor2
@decor1
def identity2(a):
    return a


print(identity1(5))             # 67
print(identity2(5))             # 2209
