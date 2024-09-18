# Scope
# 1. Local scope
# 2. Global scope

def add(previous_result):
    # Global scope
    global result
    result = previous_result + 1
    return result

# Example of local scope
result = 99
add(100)
print(result)