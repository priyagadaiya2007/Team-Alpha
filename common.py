# Calculator Program using 6 Methods

# Method 1: Addition
def add(a, b):
    return a + b

# Method 2: Subtraction
def subtract(a, b):
    return a - b

# Method 3: Multiplication
def multiply(a, b):
    return a * b

# Method 4: Division
def divide(a, b):
    if b != 0:
        return a / b
    return "Division by zero is not allowed"

# Method 5: Modulus
def modulus(a, b):
    return a % b

# Method 6: Power
def power(a, b):
    return a ** b

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Display results
print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("Multiplication =", multiply(num1, num2))
print("Division =", divide(num1, num2))
print("Modulus =", modulus(num1, num2))
print("Power =", power(num1, num2))