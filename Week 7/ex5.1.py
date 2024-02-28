num = 0
tot = 0.0
while True :
    sval = input("Enter a number: ")
    if sval == "done": #check for "done"
        break
    try:
        fval = float(sval) #Try this
    except:
        print("Invalid input") #Display this if invalid input then iterate again via Continue
        continue
    #print (fval)
    num = num + 1 #increment variable
    tot = tot + fval #increment total

#print("All done")
print(tot,num, tot/num) #print values
