def is_a_triangle(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        p = (a + b + c) / 2
        return None
    return heron(a, b, c)

print(area_of_triangle(1., 1., 2. ** 0.5))