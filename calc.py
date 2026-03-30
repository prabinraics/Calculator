# main.py

try:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Answer:", num1 + num2)

    elif choice == "2":
        print("Answer:", num1 - num2)

    elif choice == "3":
        print("Answer:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Answer:", num1 / num2)

    else:
        print("Invalid choice")

except ValueError:
    print("Error: Please enter valid numbers")
