def is_armstrong(n):
    str_n = str(n)
    power = len(str_n)
    # This loops through the string, does the math, and sums it all at once
    return sum(int(digit) ** power for digit in str_n) == n

print(is_armstrong(153))