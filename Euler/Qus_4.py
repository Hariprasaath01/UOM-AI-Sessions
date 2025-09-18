'''
Problem - Find the large palindromic number made from the product of two 2-digit numbers
'''

def is_palindrome(n): # Function to determine palindrome
    s = str(n)
    return s == s[::-1]

def largest_palindrome_product():
    largest = 0
    # Start from the largest 3-digit number
    for i in range(999, 99, -1):
        # Start j from i down to 100 to avoid duplicates and ensure larger products first
        for j in range(i, 99, -1):
            product = i * j
            # If product is less than current largest, no need to check smaller j
            if product < largest:
                break
            if is_palindrome(product):
                largest = max(largest, product)
    return largest

# Time Complexity: O(n^2) in worst case, but optimized with early breaking.
# Space Complexity: O(1)

result = largest_palindrome_product()
print(result) # Outputs the result