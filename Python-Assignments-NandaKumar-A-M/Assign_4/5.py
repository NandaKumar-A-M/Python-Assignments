sorted_list = []
n=int(input("Enter the length of the list"))
print("Enter the numbers in to list in SORTED ORDER")
for i in range(n):
    a=int(input())
    sorted_list.append(a)

target_element = int(input("Enter the element to search"))
low, high = 0, n- 1
found = False
while low <= high:
    mid = (low + high) // 2

    if sorted_list[mid] == target_element:
        print(f"Element {target_element} found at index {mid}.")
        found = True
        break
    elif sorted_list[mid] < target_element:
        low = mid + 1
    else:
        high = mid - 1  

if not found:
    print(f"Element {target_element} not found in the list.")
