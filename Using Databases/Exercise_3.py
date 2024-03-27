class PartyAnimal:
    
    def __init__(self, name): 
        self.x = 0  # Initialize a party count variable
        self.name = name  # Set the name of the party animal
        print(self.name, "constructed")  # Print a message indicating the party animal is constructed
        
    def party(self):
        self.x = self.x + 1  # Increment the party count
        print(self.name, "party count", self.x)  # Print the party count
        
class FootballFan(PartyAnimal):
    
    def __init__(self, name):
        super().__init__(name)  # Call the constructor of the parent class (PartyAnimal)
        self.points = 0  # Initialize a points variable for football fan
        print(self.name, "football fan constructed")  # Print a message indicating the football fan is constructed
        
    def touchdown(self):
        self.points = self.points + 7  # Add 7 points for a touchdown
        self.party()  # Call the party method from the parent class
        print(self.name, "points", self.points)  # Print the points
        
s = PartyAnimal("Sally")  # Create a party animal object
j = FootballFan("Jim", )  # Create a football fan object
j.party()  # Call the party method
j.touchdown()  # Call the touchdown method