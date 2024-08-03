numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = [2, 3, 5, 7, 11, 13]
Not_Primes = [4, 6, 8, 9, 10, 12, 14, 15]
i = 0
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        print(n, '- не простое и не сложное число')
        continue
    else:  f = n ** (1 / 2)
    for a in range(2, int(f + 1)):
        if n % a == 0:
            is_prime = False
            break