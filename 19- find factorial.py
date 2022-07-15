num = int(input("Give me a number: "))
new_num = 1
for n in range(num,0,-1):
    new_num = new_num*n
print(new_num)