class PartyAnimal: # This is a class
    
    def __init__(self, name): # This is a constructor
        self.x = 0 # This is a variable
        self.name = name # This is a variable
        print(self.name, "constructed") # This is a print statement
    
    def party(self): # This is a method
        self.x = self.x + 1 # This is a variable
        print(self.name, "party count", self.x) # This is a print statement
        
S = PartyAnimal("Sally") # This will construct the object
S.party() # This will print Sally party count 1
J = PartyAnimal("Jim") # This will construct the object 
J.party() # This will print Jim party count 1

J.party() # This will print Jim party count 2   
S.party() # This will print Sally party count 2