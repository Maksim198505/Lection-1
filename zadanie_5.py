# Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

def count_find_num(primesL, limit):
    global n
    n = limit
    i = 2
    prim_fac = []
    while i * i <= n:
        while n % i == 0:
            prim_fac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prim_fac.append(n)
    return prim_fac


primesL = [2, 5]
limit = 200
val = count_find_num(primesL, limit) == [8, 200]


if __name__ == '__main__':
    print(count_find_num(primesL, limit))
