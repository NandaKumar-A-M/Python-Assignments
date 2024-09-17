def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



print("Prime numbers between", 10, "and", 50, "are:")
for num in range(10, 51):
    if is_prime(num):
        print(num, end=' ')
