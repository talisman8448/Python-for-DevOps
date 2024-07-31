import sys

def add(a, b):
    addition = a + b
    return(addition)


def sub(a, b):
    subtraction = a - b
    return(subtraction)

def mul(a, b):
    multiplication = a * b
    return(multiplication)

def div(a, b):
    divison = a / b
    return(divison)

num1 = int(sys.argv[1])

operation = sys.argv[2]

num2 = int(sys.argv[3])


if operation == "add":
   output = add(num1, num2)
   print(output)
elif operation == "sub":
     output = sub(num1, num2)
     print(output)
elif operation == "mul":
     output = mul(num1, num2)
     print(output)
else:
      output = div(num1, num2)
      print(output)


