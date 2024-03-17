def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

def introduction2(last_name, first_name):
    print("Hello, my name is", last_name, first_name)

introduction2("Skywalker", "Luke")
introduction2("Quick", "Jesse")
introduction2("Kent", "Clark")

def introduction3(last_name, first_name):
    print("Hello, my name is", last_name, first_name)

introduction3(last_name = "Skywalker", first_name = "Luke")
introduction3(last_name = "Quick", first_name = "Jesse")
introduction3(last_name = "Kent", first_name = "Clark")

def introduction4(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
    
introduction4("Ian")

# Call the function here.
