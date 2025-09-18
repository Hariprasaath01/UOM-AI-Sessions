'''
Problem - Find the sum of primes below two million
'''

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i starting from i*i
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

def sum_primes_below(n):
    is_prime = sieve_of_eratosthenes(n)
    total = 0
    for i in range(2, n+1):
        if is_prime[i]:
            total += i
    return total

# Time Complexity: O(n log log n)
# Space Complexity: O(n)

result = sum_primes_below(2000000)
print(result) # Outputs the result