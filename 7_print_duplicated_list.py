list = [1,1,2,2,3,3,4]
new_list=[]
for n in list:
    if n not in new_list:
        new_list.append(n)
    else:
        print("Yes",n)