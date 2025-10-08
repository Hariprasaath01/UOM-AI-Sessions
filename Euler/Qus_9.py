'''
Problem - if a, b, c are pythogares triplen and a + b + c = 1000,
find the product abc
'''

def find_pythagorean_triplet():
    for a in range(1, 333):  # a cannot exceed 332 since a < b < c and a+b+c=1000
        for b in range(a+1, 500):  # b cannot exceed 499
            c = 1000 - a - b
            if c <= b:
                break  # since c must be greater than b
            if a*a + b*b == c*c:
                return a * b * c
    return -1

# Time Complexity: O(n^2) where n is about 1000, but optimized to O(332*500) ≈ 166,000
# Space Complexity: O(1)

result = find_pythagorean_triplet()
print(result) # Outputs the result