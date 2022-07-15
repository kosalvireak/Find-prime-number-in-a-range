num = 5642
new_num = 0
while num != 0:
    # remainder = num % 10
    # or
    #i = 1
    # new_num = new_num + (num % 10)*i
    #i = i *10
    # or
    new_num = new_num * 10 + num % 10
    num = num // 10
print(new_num)
