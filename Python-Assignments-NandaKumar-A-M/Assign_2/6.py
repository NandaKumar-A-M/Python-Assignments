st=input("Enter ur string here:\n")
st=st.upper()
dict={}
for i in st:
    if i.isalpha():
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
most_repeated=max(dict,key=dict.get)
print("The most appeared string is",most_repeated,"That is",dict[most_repeated],"Times")
print(dict)