input1= int(input("Enter first number: ")) 
input2= int(input("Enter second number: ")) 
# i = input1
# while i <= input2:
#     if (i % 2 == 1) and (i % 3 == 1 or i % 3 == 2) :
#         if  (i % 5 == 0 )or i%7 ==0:
#             if i / 5 < 2:
#                 print(i)
#         else:
#             print(i)
#     i = i + 1
for n in range(input1,input2):
    for i in range(2,n):
        if (n % i) == 0:
            break
    else:
        print(n)