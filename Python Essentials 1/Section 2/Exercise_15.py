'''
Operators: addition
The addition operator is the + (plus) sign, which is fully in line with mathematical standards.

Again, take a look at the snippet of the program below:

print(-4 + 4)
print(-4. + 8)


The result should be nothing surprising. Run the code to check it.


The subtraction operator, unary and binary operators
The subtraction operator is obviously the - (minus) sign, although you should note that this operator also has another meaning - it can change the sign of a number.

This is a great opportunity to present a very important distinction between unary and binary operators.

In subtracting applications, the minus operator expects two arguments: the left (a minuend in arithmetical terms) and right (a subtrahend).

For this reason, the subtraction operator is considered to be one of the binary operators, just like the addition, multiplication and division operators.

'''

print(-4 + 4)
print(-4. + 8)

print(9 % 6 % 2)

print(2 ** 2 ** 3)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print((2 ** 4), (2 * 4.), (2 * 4)) #16, 8.0, 8
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) #-0.5 0.5 0 -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2)) #-2 2 512