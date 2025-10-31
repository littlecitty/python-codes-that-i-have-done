#32. Create a calculator using functions.
def calcu_m(a,b):
    match signs:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case "%":
            print(a % b)
        case _:
            print("select symobl homie. ")
print("use symblos like: + for add, - for sub, etc.")

signs = input("enter a sing like: +, -, etc.")
a,b = map(int,input("enter 2 no. with sign  to add, sub,  etc. : sepearted wiith commas").strip().split(","))
calcu_m(a,b)

#Pythonic Calculator
def calculator(a: int, b: int, sign: str):
    match sign:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return "Error: Division by zero" if b == 0 else a / b
        case "%":
            return "Error: Modulo by zero" if b == 0 else a % b
        case _:
            return "Invalid operator"

print("Use symbols like: + for add, - for sub, * for multiply, / for divide, % for modulo")

# Get inputs
a, b = map(int, input("Enter 2 numbers separated by commas: ").split(","))
sign = input("Enter an operator (+, -, *, /, %): ")

# Calculate and print
result = calculator(a, b, sign)
print("Result:", result)


#short match-case calculator
def calc(a, b, op):
    match op:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/": return a / b if b else "Div by 0"
        case "%": return a % b if b else "Mod by 0"
        case _:   return "Invalid"

a, b = map(int, input("Enter 2 numbers (comma-separated): ").split(","))
op = input("Enter operator (+, -, *, /, %): ")
print(calc(a, b, op))

