# Написать метод bananas, который принимает на вход строку и
# возвращает количество слов «banana» в строке.
# (Используйте - для обозначения зачеркнутой буквы)
# Input: bbananana

def bananas(s, word):
    ret = []
    if word == '':
        ret.append(''.rjust(len(s), '-'))
        return ret

    left_s = ''
    for si in range(len(s)):
        if word[0] == s[si]:
            left_s = ''.rjust(si, '-') + s[si]
            if s[si + 1:] == '' and word[1:] == '':
                ret.append(left_s)
            else:
                right_s_list = bananas(s[si + 1:], word[1:])
                for right_s in right_s_list:
                    ret.append(left_s + right_s)
    return ret


if __name__ == '__main__':
    for s in bananas('bananaaa', 'banana'):
        print(s)
