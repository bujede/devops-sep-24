

# Return values are option
def add(previous_result): # previous_result = 100, 100+10 = 110
    res = 10 + previous_result
    return res

def addAnother(previous_result): # previous_result = 110 + 10 = 120
    res = 10 + previous_result  
    return res

def multiply(): # previous_result = 100
    res = 10 * 10
    return res

# ---------------------------
# Main program
print("Math calculation", addAnother(add(multiply())))


# ---------------------------
# Output
# 1. 30, 30
# 2. 50
# 3. 40