import sys

def add(a, b):
    addition = a + b
    return addition
def sub(a, b):
    subtract = a - b 
    return subtract
def div(a, b):
    divide = a / b
    return divide

def floor_div(a, b):
    floor_div = a // b
    return floor_div

def modules(a, b):
    mod = a % b
    return mod


num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)
elif operation == "sub":
    output = sub(num1, num2)
    print(output)
elif operation == "div":
    output = div(num1, num2)
    print(output)
elif operation == "floor_div":
    output = floor_div(num1, num2)
    print(output)
else:
    output = modules(num1, num2)
    print(output)
    