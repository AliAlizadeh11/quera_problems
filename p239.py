# t = int(input())

# numbers = list()
# for i in range(t):
#     n = int(input())
#     numbers.append(n)

def calculate_sum(n):
    pass

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(20))


def find_prime_facs(n):
    list_of_factors=[]
    i=2
    while n>1:
        if n%i==0:
            list_of_factors.append(i)
            n=n/i
            i=i-1
        i+=1  
    return set(list_of_factors)
print(find_prime_facs(20))
