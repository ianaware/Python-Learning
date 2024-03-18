'''

Define BMI function and others

'''

#Convert lbs to kg

def lbs_to_kg(lb):
    return lb * 0.45359237

print(lbs_to_kg(1))

#Convert ft and in to m

def ft_and_in_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_in_to_m(6))

#Convert bmi using weight and height

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
        weight < 20 or weight > 200:
        return None
    return weight / height ** 2

print(bmi(weight= lbs_to_kg(176), height= ft_and_in_to_m(5, 7)))
