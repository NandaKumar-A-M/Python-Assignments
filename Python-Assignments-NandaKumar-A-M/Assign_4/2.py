list = []
n=int(input("Enter the length of the list"))
print("Enter the numbers in to list")
for i in range(n):
    a=int(input())
    list.append(a)

for i in range(1, n):
    key = list[i]
    j = i - 1
    while j >= 0 and key < list[j]:
        list[j + 1] = list[j]
        j -= 1

    list[j + 1] = key
print("Sorted array:", list)
