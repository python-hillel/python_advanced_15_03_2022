# from random import randint
#
#
# class SortError(Exception):
#     def __init__(self, first, second, msg=''):
#         self.first = first
#         self.second = second
#         super().__init__(msg)
#
#     def __str__(self):
#         return f'{self.first}, {self.second}'
#
#
# class Item:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return str(self.value)
#
#
# def print_list(obj):
#     for value in obj:
#         print(value, end=' ')
#     print()
#
#
# def qsort(obj, left_idx=0, right_idx=None):
#     if right_idx is None:
#         right_idx = len(obj) - 1
#
#     if left_idx >= right_idx:
#         return
#
#     i, j = left_idx, right_idx
#     middle = obj[(left_idx + right_idx) // 2]
#     while i <= j:
#         while middle > obj[i]:
#             i += 1
#
#         while middle < obj[j]:
#             j -= 1
#
#         if i <= j:
#             obj[i], obj[j] = obj[j], obj[i]
#             i, j = i + 1, j - 1
#
#     qsort(obj, left_idx, j)
#     qsort(obj, i, right_idx)
#
#
# def test_sort(obj):
#     for i in range(len(obj) - 1):
#         if obj[i] > obj[i + 1]:
#             raise SortError(obj[i], obj[i + 1], msg='Sorting is incorrect')
#
#
# # lst = [Item(randint(10, 99)) for _ in range(25)]
# lst = [randint(10, 99) for _ in range(25)]
# print(lst)
#
# print_list(lst)
#
# # lst.sort()            # ERROR
# # qsort(lst)            # ERROR
# # test_sort(lst)        # ERROR
#
# print_list(lst)


from random import randint


class SortError(Exception):
    def __init__(self, first, second, msg=''):
        self.first = first
        self.second = second
        super().__init__(msg)

    def __str__(self):
        return f'{self.first}, {self.second}'


class Item:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


def print_list(obj):
    for value in obj:
        print(value, end=' ')
    print()


def qsort(obj, comparator, left_idx=0, right_idx=None):
    if right_idx is None:
        right_idx = len(obj) - 1

    if left_idx >= right_idx:
        return

    i, j = left_idx, right_idx
    middle = obj[(left_idx + right_idx) // 2]
    while i <= j:
        while comparator(middle, obj[i]) > 0:
            i += 1

        while comparator(middle, obj[j]) < 0:
            j -= 1

        if i <= j:
            obj[i], obj[j] = obj[j], obj[i]
            i, j = i + 1, j - 1

    qsort(obj, comparator, left_idx, j)
    qsort(obj, comparator, i, right_idx)


def item_comp(item1, item2):
    if int(str(item1)) > int(str(item2)):
        return 1
    elif int(str(item1)) < int(str(item2)):
        return -1
    else:
        return 0


def test_sort(obj, comparator, revers=False):
    for i in range(len(obj) - 1):
        if comparator(obj[i], obj[i + 1]) > 0 if not revers else comparator(obj[i + 1], obj[i]) > 0:
            raise SortError(obj[i], obj[i + 1], msg='Sorting is incorrect')


lst = [Item(randint(10, 99)) for _ in range(25)]
# lst = [randint(10, 99) for _ in range(25)]
print(lst)

print_list(lst)

# lst.sort(key=lambda x: int(str(x)), reverse=True)
# test_sort(lst, item_comp, revers=True)
# print_list(lst)

qsort(lst, item_comp)
test_sort(lst, item_comp)
print_list(lst)
