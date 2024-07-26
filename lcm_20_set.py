"""
 *   2520 is the smallest number that can be divided by each of the numbers 
 * from 1 to 10 without any remainder.
 *   What is the smallest positive number that is evenly divisible by all of
 * the numbers from 1 t0 20?
 */
 """

def lcm_of_1_to_20():
    count = 1
    divisor = 2
    while divisor<=20 :
        print(count)
        if count % divisor == 0:
            divisor += 1
        else:
            count += 1
            divisor = 2
    return count

print(lcm_of_1_to_20())