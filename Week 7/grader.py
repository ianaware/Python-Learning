def computegrade (score):
    if score < 0.0 or score > 1.0:
        print("Invalid score entered")
    elif score > 0.9:
        print("Your score is A")
    elif score > 0.8:
        print("Your score is B")
    elif score > 0.7:
        print("Your score is C")
    elif score > 0.6:
        print("Your score is D")
    elif score <= 0.6:
        print("Your score is F")

print("Welcome to the grade assessment tool!\n")
print("Enter your grade: \n")
score_string = input()
try:
    score_float = float(score_string)
    computegrade(score_float)
except:
    print("Invalid input")