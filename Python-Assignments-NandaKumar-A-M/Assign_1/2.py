numbers = (1,2,3,4,5,6,7,8,9)
even_count = 0
odd_count = 0
for num in numbers:
    if num%2 == 0:
        even_count+=1
print("even count : ",even_count)
print("odd count : ",len(numbers)-even_count)
