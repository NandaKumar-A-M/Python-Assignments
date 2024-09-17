def display_shopping_list(shopping_list):
    print("Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print()

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")


shopping_list = []

while True:
    print("Options:")
    print("1. Display Shopping List")
    print("2. Add Item to Shopping List")
    print("3. Remove Item from Shopping List")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
         display_shopping_list(shopping_list)
    elif choice == '2':
        item_to_add = input("Enter the item to add: ")
        add_item(shopping_list, item_to_add)
    elif choice == '3':
        item_to_remove = input("Enter the item to remove: ")
        remove_item(shopping_list, item_to_remove)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


