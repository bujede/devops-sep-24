

cities = [ "Mumbai", "Hyderabad", "Pune", "Chennai", "Bangalore" ]

                          # 0,1,2,3,4
totalCities = len(cities) # 1,2,3,4,5
i = 0
# while 5 >= 1: true
# while 5 >= 2: true
# while 5 >= 3: true
# while 5 >= 4: true
# while 5 >= 5: true
# while 5 >= 6: false

while totalCities >= (i + 1):
    print("Total length ", totalCities, " >= ", " Condition: ", i, " + 1 = ", (i + 1) )
    i = i + 1

print("Condition is false", i + 1)
