#yes, it has a sequel

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "can't just break the universe like that. try again."
    else:
        return a / b
    
calculator_actions = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,

}

while True: 
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. I want to leave")

    try:
        choice = int(input("so.... which one?: "))
        if choice == 5:
            print("Good")
            break
    except ValueError:
        print("==========================")
        print("Boy! no text")
        print("==========================")
        continue


    action = calculator_actions.get(choice)

    if action is None:
        print("|=========================|")
        print("don't even try")
        print("|=========================|")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("enter second number: "))
    except ValueError:
        print("Number only")
        continue

    result = action(a, b)
    print(f"===== Result: {result} =====")