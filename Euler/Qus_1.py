'''
Problem - If we list all the natural numbers below 10 that are multiple of 3 or 5, we ger 3, 5, 6 sum of them is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_multiples(limit): # Function to do it
    total = 0
    for num in range(1, limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    # Calculations
    return total

# Time Complexity: O(n) where n is the limit (1000 in this case)
# Space Complexity: O(1)

result = sum_multiples(1000) # Calling function and assigning value
print(result) # Showing Output