'''
Problem - Find the difference between sum of squares and square of sums from numbers below 100
'''

def difference(n):
    # Calculate the sum of the first n natural numbers using the formula: n*(n+1)//2
    sum_of_n = n * (n + 1) // 2
    
    # Calculate the square of the sum of the first n natural numbers
    square_of_sum = sum_of_n ** 2
    
    # Calculate the sum of the squares of the first n natural numbers using the formula: n*(n+1)*(2*n+1)//6
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    
    # Return the difference between the square of the sum and the sum of the squares
    return square_of_sum - sum_of_squares

# Time Complexity: O(1) - Constant time due to direct formula calculations
# Space Complexity: O(1) - Only a few variables are used

# Calculate the difference for the first 100 natural numbers
result = difference(100)
print(result)