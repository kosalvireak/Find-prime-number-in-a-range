#1.  Write a Python Program to print Prime Numbers between 2 numbers
input1= int(input("Enter first number: ")) 
input2= int(input("Enter second number: ")) 

for n in range(input1,input2):
    for i in range(2,n):
        if (n % i) == 0:
            break
    else:
        print(n)