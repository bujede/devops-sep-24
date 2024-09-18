# List 
cities = [ "Mumbai", "Hyderabad", "Pune", "Chennai", "Bangalore" ]

# Set
set1 = {3, 4, 5, 1, 2}

# Dictionary
empData = {
    'ID': 1,
    'Name': 'Bilal',
    'City': 'Pune',
    'Skills': 'DevOps',
} # Key value pairs # Java Map

# # cities
# print(cities)
# print(cities[0])
# cities[0] = "Delhi"
# print(cities)
# cities.remove("Delhi")
# print(cities)
# print(cities[0])

# set
print(set1)
set1.add("Delhi")
print(set1)
set1.add("Mumbai")
print(set1)
set1.add("Mumbai")
print(set1)
set1.add("Hyderabad")
# set1.remove("Mumbai")
# print(set1)
# Check if "Mumbai" is in the set
# print("Mumbai" in set1)

if "Mumbai" in set1:
    print("Mumbai is in the set")
else:
    print("Mumbai is not in the set")

# Loop through the set
# Scope of item is within the loop
length = len(set1)
print("length of set1: ", length)

for item in set1:
    if item == "Mumbai":
        print("Mumbai is in the set")