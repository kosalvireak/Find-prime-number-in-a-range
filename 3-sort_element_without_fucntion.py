list = [8, 5, 4, 6, 2, 3,3, 9,12,43,1]
new_list = []
m = 0
min = 100
while len(list) > 0:
    for i in range(0, len(list)):
        if int(list[i]) < min:
            min = list[i]    # we found min
    #new_list.insert(m, min)  # assign that min to new list
    new_list.append(min)
    list.remove(min)
    m = m + 1
    min = 100
print(new_list)
