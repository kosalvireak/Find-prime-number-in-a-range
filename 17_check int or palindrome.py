num = 564657
def check_num(num):
    new_num = 0
    while num != 0:
        new_num = new_num * 10 + num % 10
        num = num // 10
    return new_num
you = check_num(num)
if you - num == 0:
    print(True)
else:
    print(False)

# Without function

num = 56465
temp = num
new_num = 0
while num != 0:
    new_num = new_num * 10 + num % 10
    num = num // 10
if temp == new_num:
    print(True)
else:
    print(False)
