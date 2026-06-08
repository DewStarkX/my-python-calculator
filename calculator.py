#if you have any problem, fight me
while True:
    print("Welcome to THE calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    try:
        input1 = int(input("Selecting function:"))
    except ValueError:
        print("don't even try")
        continue

    if input1 not in [1, 2, 3, 4]:
        print("|=========================================================|")
        print("nuh uh")
        print("|=========================================================|")
        continue


    try:

        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("please... only number")
        continue

    try:
        if input1 > 4:
            print("Error")

        elif input1 == 1:
            print("|===============|")
            print("result :", a + b)
            print("|===============|")
            break

        elif input1 == 2:
            print("|===============|")
            print("result: ", a - b)
            print("|===============|")
            break

        elif input1 == 3:
            print("|===============|")
            print("result: ", a * b)
            print("|===============|")
            break

        elif input1 == 4:
            if b != 0:
                print("|================|")
                print("result : ", a / b)
                print("|================|")
                break
            else: 
                print("================")
                print("DON'T")
                print("|================|")
                break
    except ValueError:
        continue