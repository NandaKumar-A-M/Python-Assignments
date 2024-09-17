list=[]
sentence=input("Enter the string with numbers: ")
for i in sentence:
    if i.isdigit():
        #print(type(sentence),i)
        list.append(i)
print(list)
# for i in list:
#     print(i,end='')
print("\nTotal numbers:",len(list))
