

cities = [ "Mumbai", "Hyderabad", "Pune", "Chennai", "Bangalore" ]


# Logical related code lines are grouped together in a function
def print_city(city):
    print(city, ": Pune is in the list")
    print("Line code 1 ")
    print("Line code 2 ")
    print("Line code 3 ")
    print("Line code 4 ")
    print("Line code 5 ")
    print("Line code 6 ")
    print("Line code 7 ")
    print("Line code 8 ")
    print("Line code 9 ")
    print("Line code 10 ")
    
# Loop through the list of cities
for city in cities:
    # Check if pune is in the list
    if city == "Pune":
        print_city(city)
        break



