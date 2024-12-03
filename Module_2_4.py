number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(number)):
    k = int(i)
    if k < 2:
        continue
    is_prime = True
    for j in range(2, k):
        if k % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(k)
    else:
        not_primes.append(k)
print(primes)
print(not_primes)