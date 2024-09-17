list=[]
numbers=[1,2,3,4,5,6,7,8,9,0]
#print(type(numbers[1]))
strnumb=str(numbers)
sentence=input("Enter the string with numbers: ")
for i in sentence:
    if i==" ":
        continue
    elif i in strnumb:
        list.append(i)
for i in list:
    print(i,end='')
print("\nTotal numbers:",len(list))
