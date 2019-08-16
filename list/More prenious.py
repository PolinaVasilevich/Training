list_num = input().split()
new_list = []
for i in range(1, len(list_num)):
    if int(list_num[i]) > int(list_num[i - 1]):
        new_list.append(list_num[i])
print(' '. join(new_list))
