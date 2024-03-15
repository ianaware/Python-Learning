list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

list_a = ["A", "B", "C"]
list_b = list_a
list_c = list_b

del list_a[0]
del list_b

print(list_c)

list_e = ["A", "B", "C"]
list_f = list_e
list_g = list_f

del list_e[0]
del list_f[:]

print(list_g)

my_list = [1, 2, "in", True, "ABC"]

print (1 in my_list)
print ("A" not in my_list)
print (3 not in my_list)
print (False in my_list)

z = 10
y = 0
x = z > y or z == y

my_list_4 = [3, 1, -1]
my_list_4[-1] = my_list_4[-2]
print(my_list_4)
       
vals = [0, 1, 2]
vals[0], vals[1] = vals[1], vals[2]

print(vals) 

nums = []
vals2 = nums[:]
vals2.append(1) 

print(nums)
print(vals2)

my_list6 = [0 for i in range(1, 3)]
print(my_list6)

my_list7 = [0, 1, 2, 3]
x = 1
for elem in my_list7:
    x *= elem
print(x)

