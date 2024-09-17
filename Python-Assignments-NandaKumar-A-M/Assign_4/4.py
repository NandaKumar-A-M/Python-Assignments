list = []
n=int(input("Enter the length of the list"))
print("Enter the numbers in to list")
for i in range(n):
    a=int(input())
    list.append(a)

Skey = int(input("Enter the element to search: "))
found = False
for i, element in enumerate(list):
    if element == Skey:
        print(f"Element {Skey} found at index {i}.")
        found = True
        break

if not found:
    print(f"Element {Skey} not found in the list.")