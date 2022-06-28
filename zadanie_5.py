# Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

from functools import reduce as red


def count_find_num(primesL, limit):
    if red(lambda a, b: a * b, primesL) > limit:
        return []
    result = list()
    result.append(red(lambda a, b: a * b, primesL))
    for i in primesL:
        for prim_fac in result:
            prim_fac *= i
            while prim_fac <= limit and prim_fac not in result:
                result.append(prim_fac)
                prim_fac *= i
    return [len(result), max(result)]


if __name__ == '__main__':
    primesL = list(map(int, input().split()))
    limit = int(input())
    print(count_find_num(primesL, limit))
