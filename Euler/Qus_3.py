'''
Probem - Finding the largest prime factor
'''

def largest_prime_factor(n):
    # Divide by 2 until n is odd
    while n % 2 == 0:
        n //= 2
    # If n becomes 1, then 2 is the largest prime factor
    if n == 1:
        return 2
    
    # Now n is odd, check for odd factors starting from 3
    factor = 3
    # Iterate up to the square root of n
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2
    # If n is greater than 1, then n is prime and the largest factor
    if n > 1:
        return n
    else:
        return factor - 2  # Last factor that divided n

# Time Complexity: O(sqrt(n)), where n is 600851475143
# Space Complexity: O(1)

result = largest_prime_factor(600851475143)
print(result) # Outputs the result