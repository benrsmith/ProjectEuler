primeFactors = []

def isPrime(n):
    for i in range(1,int(n**0.5)+1):
        if n%i == 0 and i!=1 and i!= n:
            return False
    return True


def factors(n):
    factors = []
    for i in range(1,int(n**0.5) + 1):
        if n%i == 0 and i!= 1 and i!= n:
            factors.append(i)
    return factors

for num in factors(600851475143):
    if isPrime(num):
        primeFactors.append(num)

print (max(primeFactors))
