from random import randint
import sys


def countdown_1(num):
    lst = []
    while num > 0:
        lst.append(num-1)
        num -= 1
    return lst


print(countdown_1(15))


def countdown_2(num):
    print('Start')
    while num > 0:
        yield num - 1
        num -= 1


# print(countdown_2(15))
# print(countdown_2(15))
gen = countdown_2(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

for value in countdown_2(10):
    print(value, end=' ')
print()


def random_gen(start, stop, cnt):
    # from random import randint
    while cnt > 0:
        yield randint(start, stop)
        cnt -= 1


for value in random_gen(10, 99, 10):
    print(value, end=' ')
print()


# lst = [выражение1 выражени2 выражение3]
# lst = [выражение1 выражени2]

# lst = [randint(10, 99) for _ in range(15000000)]
# print(lst)
# print(sys.getsizeof(lst))

# lst1 = [value for value in lst if value % 2 != 0]
# print(lst1)
# print(sys.getsizeof(lst1))

# gen = (value for value in lst if value % 2 != 0)
# print(sys.getsizeof(gen))
# print(type(gen), gen)
# for value in gen:
#     print(value, end=' ')
# print()


lst1 = [value for value in range(10**8) if value % 2 != 0]
print(sys.getsizeof(lst1))

gen = (value for value in range(10**8) if value % 2 != 0)
print(sys.getsizeof(gen))
