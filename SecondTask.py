import random
import string

s = '5ADadc1!!! s6d2,./ dv6/v3'
s = s.split()
print(s)
for i, word in enumerate(s, 0):
    for j, letter in enumerate(word):
        if letter not in string.ascii_letters:
            #word = word.replace(letter, '')
    s = str(s).replace(word, '')
print(s)
#for i, item in enumerate(s):
   # s = s.replace(item, item[::-1])
#print(s)
