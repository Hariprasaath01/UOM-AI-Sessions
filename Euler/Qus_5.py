'''
Probem - Find the smalest divisible number by every numbers
between 1 and 20
'''

def gcd(a, b): # Function to find GCD
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): # Function to find LCM
    return a * b // gcd(a, b)

def smallest_multiple(n): # Function to find the result
    result = 1
    for i in range(2, n+1):
        result = lcm(result, i)
    return result

# Time Complexity: O(n * log(min(a, b))) where n is 20.
# Space Complexity: O(1)

result = smallest_multiple(20)
print(result) # Outputs resut