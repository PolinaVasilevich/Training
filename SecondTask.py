import random


def string_conversion(s):
    letter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    a = []
    for i in range(len(s)):
        if s[i] in letter:
            a.append(s[i])
    return ''.join(a)


def magic_function(s):
    s = s.split()
    b = []
    for i in range(len(s)):
        b.append(''.join(list(s[i])[::-1]))
    return ' '.join(random.sample(b, len(b)))


if __name__ == '__main__':
    print(magic_function(string_conversion('I dah ot evom tuo')))
