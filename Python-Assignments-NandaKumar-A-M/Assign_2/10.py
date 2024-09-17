
expenses = {}

while True:
    print("\nExpense Menu:")
    print("1. Add new entry")
    print("2. Remove entry")
    print("3. Display summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        day = input("Enter the day for the new entry: ")
        expense = float(input(f"Enter expenses for {day}: $"))
        expenses[day] = expense
        print("Entry added successfully!")

    elif choice == '2':
        day_to_remove = input("Enter the day to remove the entry: ")
        if day_to_remove in expenses:
            del expenses[day_to_remove]
            print("Entry removed successfully!")
        else:
            print("Entry not found. Please enter a valid day.")

    elif choice == '3':
        total_expenses = sum(expenses.values())
        remaining_budget = float(input("\nEnter your weekly budget: $")) - total_expenses

        print("\nExpense Summary:")
        for day, expense in expenses.items():
            print(f"{day}: ${expense:.2f}")

        print(f"\nTotal Expenses for the Week: ${total_expenses:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

    elif choice == '4':
        print("Exiting the expense tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

