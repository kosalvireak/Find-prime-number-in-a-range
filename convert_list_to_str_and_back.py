list = ['8', '5', '4', '3', '6', '2', '3', '4', '9']
new_list = ''.join(list)
print(new_list)
#take sting and convert into list
i = 0
old_list = []
while i < len(new_list):
    old_list.append(new_list[i])
    i = i + 1
print(old_list)