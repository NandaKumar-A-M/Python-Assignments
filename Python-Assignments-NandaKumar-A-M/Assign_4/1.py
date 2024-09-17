list=[]
n=int(input("Enter the length of the list"))
print("Enter the numebers")
for i in range(n):
    z=int(input())
    list.append(z)
for i in range(n):
    for j in range(0,n-i-1):
        if list[j]>list[j+1]:
            list[j]=list[j+1]
            list[j+1]=list[j]

print("Sorted list is ",list)