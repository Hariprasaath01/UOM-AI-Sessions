'''
Problem - Find 10001 th prime number
'''

import math

def is_prime(num, primes):
    # Check divisibility by primes up to sqrt(num)
    sqrt_num = int(math.sqrt(num)) + 1
    for p in primes:
        if p > sqrt_num:
            break
        if num % p == 0:
            return False
    return True

def nth_prime(n):
    primes = [2]  # Start with the first prime
    num = 3       # Start checking from 3
    while len(primes) < n:
        if is_prime(num, primes):
            primes.append(num)
        num += 2  # Skip even numbers
    return primes[-1]

# Time Complexity: O(n * sqrt(n)) approximately, but optimized by checking only primes and up to sqrt(n)
# Space Complexity: O(n) to store the list of primes

result = nth_prime(10001)
print(result) # Outputs the result