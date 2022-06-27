# Написать метод zeros, который принимает на вход целое число (integer) и
# возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
# Будьте осторожны 1000! имеет 2568 цифр.
# Доп. инфо: http://mathworld.wolfram.com/Factorial.html

def zeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    return int(count)


if __name__ == '__main__':
    print(zeros(0))
    print(zeros(6))
    print(zeros(30))
