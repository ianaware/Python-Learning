'''

Estimated time
20 minutes

Level of difficulty
Intermediate

Objectives
becoming familiar with the concept of numbers, operators and arithmetic operations in Python;
understanding the precedence and associativity of Python operators, as well as the proper use of parentheses.
Scenario
Your task is to complete the code in order to evaluate the following expression:


The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

'''

x = float(input("Enter value for x: "))

x = 1  # Sample input
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))  # Translating the given mathematical expression into code
print("y =", y)
