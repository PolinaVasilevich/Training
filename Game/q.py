string = '|1|2|3|\n|4|5|6|\n|7|8|9|'
s = string.split('|')
print(string)
while True:
    n = input('First: ')
    indexN = s.index(n)
    s[indexN] = '0'
    print('|'.join(s))
    if s.count('0') == 3:
        print('You win!')
        break
    m = input('Second: ')
    indexM = s.index(m)
    s[indexM] = 'X'
    print('|'.join(s))
    if s.count('X') == 3:
        print('You win!')
        break
