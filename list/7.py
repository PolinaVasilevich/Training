list_num = input().split()

index_max_num = list_num.index(str(max(map(int, list_num))))
index_min_num = list_num.index(str(min(map(int, list_num))))

list_num[index_max_num], list_num[index_min_num] = \
    list_num[index_min_num], list_num[index_max_num]

print(' '.join(list_num))
