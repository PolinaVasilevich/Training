import random


def string_conversion(s):
    letter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = s.split()
    res = []
    for word in s:
        a = ''
        for l in word:
            if l in letter:
                a += l
        res.append(a)
    return ' '.join(res)


def magic_function(s):
    s = s.split()
    b = []
    for i in range(len(s)):
        b.append(''.join(list(s[i])[::-1]))
    return ' '.join(random.sample(b, len(b)))


if __name__ == '__main__':
    print(magic_function(string_conversion('I45 dah556 ot! evom!DDDDD tuoGGG')))
    print(string_conversion('qwef dfjdf fjdfj'))