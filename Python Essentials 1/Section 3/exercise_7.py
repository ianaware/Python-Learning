x = 5
y = 10
z = 8

print(x > y) #false
print(y > z) #true

x, y, z = 5, 10, 8 #x = 5, y = 10, z = 8

print(x > z) #false
print((y - 5) == x) #true

x, y, z = 5, 10, 8 #x is 5, y is 10, z is 8
x, y, z = z, y, x #x is 8, y is 10, z is 5

print(x > z) #true
print((y - 5) == x) #true

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four") #print this
if int(x) == 1:
    print("five") #print this
else:
    print("six")

x = 1
y = 1.0
z = "1"

if x == y:
    print("one") #print this
if y == int(z):
    print("two") #print this
elif x == y:
    print("three")
else:
    print("four") 