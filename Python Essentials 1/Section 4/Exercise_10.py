def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

a = float(input('Enter the first side\'s length:'))
b = float(input('Enter the second side\'s length:'))
c = float(input('Enter the third side\'s length:'))

if is_a_triangle(a, b, c):
    print('Yes, it can form a triangle.')
else:
    print('No, it cannot form a triangle.')