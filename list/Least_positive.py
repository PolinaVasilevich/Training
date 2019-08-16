list_num = input().split()
list_min_num = []
for i, element in enumerate(list_num):
    if int(element) > 0:
        list_min_num.append(element)
print(min(list(map(int, list_min_num))))
