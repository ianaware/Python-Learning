class PartyAnimal: # This is a class
    def __init__(self): # This is a constructor
        self.x = 0 # This is a variable
        print("I am constructed") # This is a print statement
    
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
        
    def __del__(self): # This is a destructor
        print("I am destructed", self.x) # This is a print statement
        
an = PartyAnimal() # This will construct the object

an.party() # This will print 1
an.party() # This will print 2
an = 42 # This will destruct the object
print("an contains", an) # This will print 42
print("Type", type(an)) # This will print <class 'int'>
print(dir(an)) # This will print all the methods that can be used with an integer