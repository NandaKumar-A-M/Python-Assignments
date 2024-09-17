vowels=['a','e','i','o','u']
string=input("Enter the string here: ").lower()
vowelCnt=0
consCnt=0
for i in string:
    if i in vowels:
        vowelCnt+=1
    else:
        consCnt+=1
cons=consCnt-vowelCnt
print("Vowels appear",vowelCnt,"Times")
print("Consonent appears",cons,"Times")
