from random import randrange
Ran_num = randrange(100)
print("You have 5 chances to guess the number.")
i = 0
while i <= 7:
    i += 1
    if 6-i == 0:
        print("The answer is: " , Ran_num)
        break
    user = int(input('You have ' +str(6-i)+' chance >> Enter number from 1 to 100: '))
    #user = int(input('Choose a number between 1 and 100. You have ' + str(i) + ' guesses left. '))
    if user == Ran_num:
        print("You got it! ")
        break
    elif user < Ran_num:
        print("Your number is smaller")
    else:
        print("You number is bigger")
