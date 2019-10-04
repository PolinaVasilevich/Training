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
        if (s[1] == '0' and s[2] == '0' and s[3] == '0') or (s[1] == '0' and s[5] == '0' and s[9] == '0') or \
                (s[9] == '0' and s[10] == '0' and s[11] == '0') or (s[11] == '0' and s[7] == '0' and s[3] == '0') or \
                (s[1] == '0' and s[6] == '0' and s[11] == '0') or (s[3] == '0' and s[6] == '0' and s[9] == '0'):
            print('You win!')
            answer = input('Do you want to play? Y&N: ')
            if answer == 'N':
                break
    else:
        print('Ячейка уже занята!\nПопробуйте ещё раз.')



