# Написать метод bananas, который принимает на вход строку и
# возвращает количество слов «banana» в строке.
# (Используйте - для обозначения зачеркнутой буквы)
# Input: bbananana

from itertools import combinations as combos


def bananas(s):
    result = set()
    pattern = 'banana'
    for combo in combos(enumerate(s), 6):
        word = ['-' for _ in range(len(s))]
        z = 0
        for i, letter in combo:
            if letter == pattern[z]:
                word[i] = letter
                z += 1
            else:
                break
        if z == len(pattern):
            result.add(''.join(word))
    return result


if __name__ == '__main__':
    s = input()
    print(bananas(s))
