import math

def is_prime(n):
    # 1. Base cases: 0, 1, and negative numbers are not prime
    if n <= 1:
        return False
        
    # 2. 2 is the only even prime number
    if n == 2:
        return True
        
    # 3. Any other even number is not prime
    if n % 2 == 0:
        return False

    # 4. Check for odd factors from 3 up to the square root of n
    # We step by 2 (3, 5, 7...) because we already eliminated even numbers
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False  # We found a factor, so it's not prime

    return True  # No factors found, the number is prime