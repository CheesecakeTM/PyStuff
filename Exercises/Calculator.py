
def calc(a, b, op):

# Creates a dictionary with four key-value pairs
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Error: Division by zero"
        # On the division there is the condition to check division by zero

    }.get(op, "Invalid operation")
    # Retrieve the value from the dictionary based on the "op" argument
    # If "op" is not valid "Invalid operation" is returned


result = calc(10, 5, '+')

print(result)
