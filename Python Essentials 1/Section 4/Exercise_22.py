try:
    value = int(input("Enter a number: "))
    print("The reciprocal of the number is", 1 / value)
except ValueError:
    print("I do not know what to do")
except ZeroDivisionError:
    print("Division by zero is not allowed")