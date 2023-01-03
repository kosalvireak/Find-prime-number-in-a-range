def my_function(x):
  return x[::-1]
m = str(input("E: "))
mytxt = my_function(m)
if m == mytxt:
    print("This is palindrom")
else: print("This is not palindrom")
print(mytxt)