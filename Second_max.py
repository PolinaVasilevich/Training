s = list(map(int, input().split()))
max_s = 0
index_max_s = 0
for i, element in enumerate(s):
    if element >= max_s:
        max_s = element
        index_max_s = i
print(max_s, index_max_s)
