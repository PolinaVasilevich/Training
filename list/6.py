list_num = input().split()
tmp = 0
for i in range(1, len(list_num), 2):
    tmp = list_num[i]
    list_num[i] = list_num[i - 1]
    list_num[i - 1] = tmp
print(' '.join(list_num))
