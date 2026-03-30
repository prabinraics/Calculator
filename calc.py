def add_numbers():
    print("Addition Calculator")
    print("Enter numbers one by one.")
    print("Type 'done' when finished.")

    total = 0
    while True:
        user_input = input("Enter a number (or 'done'): ")

        if user_input.lower() == "done":
            break
        try:
            number = float(user_input)
            total += number
        except ValueError:
            print("Enter a invalid number. Please try again.")

    print("Total Sum =", total)

add_numbers()