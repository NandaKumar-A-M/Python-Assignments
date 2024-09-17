import random
genRandom=random.randint(1,100)
print("A random number got generated in range 1 to 100!\nGuess it!!!")

#print(genRandom)

bonus=5
for i in range (5):
    num=int(input(f"Guess ur {i+1}/5 th try: "))
    if num==genRandom:
        print("U guessed it")
        break 
    else:
        
        diff=genRandom-num
        if genRandom>num and diff>10 :
            print("Guess too high!!! Difference is more than 10")
        elif genRandom>num and diff<10:
            print("Guess little high!!! Difference is less than 10")
        elif genRandom<num and diff>-10:
            print("Guess little low!!! Difference is less than 10")
        elif genRandom<num and diff<-10:
            print("Guess too low!!! Difference is more than 10")
    bonus-=1
       
print("----U earned Bonus of",bonus,"out of 5 Points----")
if bonus==0:
    print("------U FAILED IN GUESSING, THE NUMBER IS--->>",genRandom)