def my_function():
   global var
   var = 2
   print("Do I know that variable?", var)


var = 1
my_function()
print(var)

def my_function2(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function2(var)
print(var)
