num = 5642
new_num = 0
while num != 0:
    remainder = num % 10
    # new_num = new_num  + remainder *i
    # or
    # new_num = new_num + (num % 10)*i
    # or
    new_num = new_num * 10 + remainder
    num = num // 10
print(new_num)
