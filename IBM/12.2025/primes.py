
sieve = [1] * pow(10, 5)
sieve[0] = sieve[1] = 0


def get_primes(N, k):
    for i in range(2, N):
        if sieve[i]:
            for j in range(i*i, N, i):
                sieve[j] = 0

    primes = [i for i,x in enumerate(sieve) if x and i%2==1]
    return primes[:k]


def get_evens(N):
    return [i for i in range(2, 2*N+1, 2)]


def is_prime(x):
    return sieve[x] == 1


def pairwise_sums(N):
    primes = get_primes(10**5, N)
    evens = get_evens(N)

    res = 0
    for i in range(len(primes)):
        for j in range(len(evens)):
            if is_prime(primes[i] + evens[j]):
                res += 1
    return res

if __name__ == '__main__':
    print([pairwise_sums(i) for i in range(1, 51)])