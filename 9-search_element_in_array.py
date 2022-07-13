arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
user_input = input("Enter 1 alphabet: ")

def find(alphabet):
    for i in range(0,len(arr)):
        if arr[i] == alphabet:
            print("Found it at position:",i)
            break
print(find(user_input))
#print("Sorry! We can't find it.")

