try:
    word = input("Enter a word: ")
    
    if not word.isalpha():
        raise TypeError("Invalid input. Please enter a word.")

    if len(word) > 50:
        raise ValueError("Word is too long. Maximum length is 50 characters.")
    
    print("Entered word:", word)

except TypeError as ty:
    print(f"TypeError: {ty}")

except ValueError as va:
    print(f"ValueError: {va}")
