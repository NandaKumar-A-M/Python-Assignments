def number_guess():
   
    print("Think of a number, and I will guess it.")
    print("Answer with 'yes' or 'no'.\n")

    lower_bound = 1
    upper_bound = 100

    while True:
        guess = (lower_bound + upper_bound) // 2
        response = input(f"Is your number {guess}? (yes/no): ").lower()

        if response == 'yes':
            print(f"\nI guessed it. Your number is {guess}.")
            break
        elif response == 'no':
            higher_lower = input("Is your number higher or lower than my guess? (higher/lower): ").lower()

            if higher_lower == 'higher':
                lower_bound = guess + 1
            elif higher_lower == 'lower':
                upper_bound = guess - 1
            else:
                print("Invalid input. Please enter 'higher' or 'lower'.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


number_guess()
