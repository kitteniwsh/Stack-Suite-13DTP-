import random


def primes(n):
    """https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


x = primes(1000)

P = random.choice(x)
Q = random.choice(x)

C = P*Q

print(f"Composite {C} should be in the database")
print(f"Primes {P} and {Q} should be in the database")
print(
    f"SELECT value FROM 'Composite' WHERE value={C} UNION SELECT value FROM 'Primes' WHERE value in ({P},{Q})")
