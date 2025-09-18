'''
Problem - Find the sum of all even-valued terms in the Fibonacci sequence that do not exceed four million. 
The Fibonacci sequence starts with 1 and 2, and each subsequent term is the sum of the previous two terms
'''

def sum_even_fibonacci(limit):
    # Initialize the first two terms of the Fibonacci sequence
    a, b = 1, 2
    total = 0
    
    # Continue until the current term exceeds the limit
    while a <= limit:
        # Check if the current term 'a' is even
        if a % 2 == 0:
            total += a
        
        # Generate the next Fibonacci term: a becomes b, and b becomes a + b
        a, b = b, a + b
    
    return total

# Time Complexity: O(log(limit)) because the Fibonacci sequence grows exponentially, 
# so the number of terms generated until exceeding the limit is logarithmic.
# Space Complexity: O(1), only a few variables are used.

result = sum_even_fibonacci(4000000)
print(result) # Outputs result