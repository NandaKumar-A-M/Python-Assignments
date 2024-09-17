list = []
n=int(input("Enter the length of the list"))
print("Enter the numbers in to list")
for i in range(n):
    a=int(input())
    list.append(a)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if list[j] < list[min_index]:
            min_index = j
    list[i], list[min_index] = list[min_index], list[i]


print("Sorted list:", list)