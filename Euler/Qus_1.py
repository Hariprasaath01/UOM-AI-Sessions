def sum_multiples(limit):
    total = 0
    for num in range(1, limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total

# Time Complexity: O(n) where n is the limit (1000 in this case)
# Space Complexity: O(1)

result = sum_multiples(1000)
print(result)