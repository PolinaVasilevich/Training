string = '|1|2|3|\n|4|5|6|\n|7|8|9|'
s = string.split('|')
print(string)
while True:
    n = input('First gamer: ')
    if n in s:
        indexN = s.index(n)
        s[indexN] = '0'
        print('|'.join(s))
        if (s[1] == '0' and s[2] == '0' and s[3] == '0') or (s[1] == '0' and s[5] == '0' and s[9] == '0') or \
                (s[9] == '0' and s[10] == '0' and s[11] == '0') or (s[11] == '0' and s[7] == '0' and s[3] == '0') or \
                (s[1] == '0' and s[6] == '0' and s[11] == '0') or (s[3] == '0' and s[6] == '0' and s[9] == '0'):
            print('First gamer win!')
            answer = input('Do you want to play? Y&N: ')
            if answer == 'N':
                break
    else:
        print('Ячейка уже занята!\nПопробуйте ещё раз.')
        n = input('First gamer: ')

    m = input('Second gamer: ')
    if m in s:
        indexN = s.index(m)
        s[indexN] = 'X'
        print('|'.join(s))
        if (s[1] == 'X' and s[2] == 'X' and s[3] == 'X') or (s[1] == 'X' and s[5] == 'X' and s[9] == 'X') or \
                (s[9] == 'X' and s[10] == 'X' and s[11] == 'X') or (s[11] == 'X' and s[7] == 'X' and s[3] == 'X') or \
                (s[1] == 'X' and s[6] == 'X' and s[11] == 'X') or (s[3] == 'X' and s[6] == 'X' and s[9] == 'X'):
            print('Second gamer win!')
            answer = input('Do you want to play? Y&N: ')
            if answer == 'N':
                break
    else:
        print('Ячейка уже занята!\nПопробуйте ещё раз.')
        m = input('Second gamer: ')

