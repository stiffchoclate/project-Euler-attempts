"""
The prime factors of 13195 are 5,7,13, and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math

def isPrime(n:int):
    print(" I defo have the answer, right now. Just need to check if ")
    return True
    


def lpf(n:int, factor:int):
    while factor <= n/2:
        if n%factor==0:
            return lpf(n/factor, 2)
        else:
            return lpf(n, factor+1)

    return factor

def lpf_2():
    n = 600851475143
    factors = set()
    count = 2
    while count< n/2 :
        if n % count == 0:
            # print(count)
            factors.add(count)
            n /= count
            count = 2
        else:
            count += 1
    factors.add(n)
    print(factors)
    #factors = sorted([x for x in factors if isPrime(x) == True])
    factors = sorted(factors)
    return factors[-1]
    
def main():
    return lpf_2()

print(main())