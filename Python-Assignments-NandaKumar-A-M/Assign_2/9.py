def cel(celsius):
    fahren=(celsius * 9/5) + 32
    print(fahren,"fahrenheits")

def fah(fahrenheit):
    cels=(fahrenheit - 32) * 5/9
    print(cels,"celsius")



ch=int(input("Choose\n1:To convert to fahrenheit\n2:To convert to celsius\n"))
if ch==1:
    celsius=float(input("Enter the celsius"))
    cel(celsius)
elif ch==2:
    fahrenheit=float(input("Enter the fahrenheit"))
    fah(fahrenheit)
else:
    print("Enter the valid choice i.e., 1 or 2")