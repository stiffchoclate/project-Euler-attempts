#Problem 5: Smallest Multiple

#What is the smallest positive numbers that is evenly divisible by all og the numbers from 1 to 20?



class IntegerSet:
    def __init__(self) -> None:
        pass
    #add getSet method
    #add prime factors
    #add factor count
    #add 

def prime_factors(n:int) -> list:
    number = n 
    factors = set()
    factor_count = {}
    count = 2
    while count < number/2:
        if n % count == 0: 
            number /= count
            factors.add(count)
            try:
                factor_count[f'{count}'] += 1
            except:
                factor_count[f'{count}'] = 1
            finally:
                count = 2
        else:
            count += 1
    
    try:
        factor_count[f'{int(number)}'] += 1
    except:
        factor_count[f'{int(number)}'] = 1

    factors.add(int(number))
    print(factors)
    return factor_count

print(prime_factors(6))
