def add(a, b):
    return a + b
    

def subtract(a, b):
    return a - b
    

def multiply(a, b):
    return a * b
    

def divide(a, b):
    return a / b
    

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

def calculate(operation, a, b):
    return operations[operation](a, b)

# Example usage
print(calculate("add", 5, 3))  # Expected output: 8