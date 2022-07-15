number = int (input('Type a integer number:') )
while number!=0:
    remainder = number % 10
    if(remainder!=0 and remainder!=1):
        print('Number is not in bynary representation!')
        break
    number = number//10
    if(number==0):
        print('Number is in bynary representation!')
