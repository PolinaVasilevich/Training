string = '|1|2|3|\n|4|5|6|\n|7|8|9|'
s = string.split('|')
print(string)
while True:
    n = input('First gamer: ')
    if n in s:
        indexN = s.index(n)
        print(indexN)
        s[indexN] = '0'
        print('|'.join(s))
        if s[1] == '0' and s[2] == '0' and s[3] == '0':
            print('You win!')
            break
    else:
        print('Ящейка уже занята!')



