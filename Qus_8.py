'''
Problem - Find the thirteen adjacent digits in the 1000 digit number that have the greatest product. What is the value of this product
'''

def main():
    # The 1000-digit number as a string
    num_str = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "668966489504452445231617318564039098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "5369781797846114664955149290862569321978468622482"
        "83972241375657956657490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "242190226710556263211119937054421750694165896048"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524663689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )
    
    # Convert the string to a list of integers
    digits = [int(d) for d in num_str]
    n = len(digits)
    k = 13
    
    # Initialize the product for the first window
    current_product = 1
    # Count zeros in the current window to avoid division by zero
    zero_count = 0
    
    # Initialize the first window
    for i in range(k):
        if digits[i] == 0:
            zero_count += 1
        else:
            current_product *= digits[i]
    
    max_product = 0 if zero_count > 0 else current_product
    
    # Slide the window
    for i in range(k, n):
        # Remove the leftmost digit of the previous window
        left_digit = digits[i - k]
        if left_digit == 0:
            zero_count -= 1
        else:
            current_product //= left_digit
        
        # Add the new digit to the window
        new_digit = digits[i]
        if new_digit == 0:
            zero_count += 1
        else:
            current_product *= new_digit
        
        # If there are no zeros in the current window, update max_product
        if zero_count == 0:
            if current_product > max_product:
                max_product = current_product
        else:
            # If there are zeros, the product is zero, so no need to update
            pass
    
    print(max_product)

# Time Complexity: O(n), where n is the number of digits (1000)
# Space Complexity: O(1)

if __name__ == "__main__":
    main()