def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Please provide valid numbers."

def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Please provide valid numbers."

def multiply(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Please provide valid numbers."