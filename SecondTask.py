import random
import string

s = '5ADadc1!!! s6d2,./ dv6/v3'

for i, item in enumerate(s):
    if item not in string.ascii_letters:
        s = s.replace(item, '')
print(s)
s = s.split()

for i, item in enumerate(s):
    s = str(s).replace(item, item[::-1])
print(s)
