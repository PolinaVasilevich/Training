import random
import string

s = '5ADadc1!!! s6d2,./ dv6/v3'
s = s.split()
print(s)
for i, word in enumerate(s):
    for j, letter in enumerate(word):
        if letter not in string.ascii_letters:
            word = word.replace(letter, '')


#for i, item in enumerate(s):
   # s = s.replace(item, item[::-1])
#print(s)
