import math

N = int(input())

mod = 10 ** 9 + 7
count_dict = {}
ans = 1

def primes(x):
    if x < 2: 
        return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, x, prime):
            primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

def cal(n):
    global count_dict
    for i in count_dict.keys():
        if n % i == 0:
            count_dict[i] += 1
            n //= i
            return n

    

for i in primes(100):
    count_dict[i] = count_dict.get(i-1, 0)

if N > 1:
    for i in range(2, N+1):
        while True:
            i = cal(i)
            if i == 1:
                break


for i in count_dict.values():
    if i != 0:
        ans *= (i+1)

print(ans % mod)