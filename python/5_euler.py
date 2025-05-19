# euler(): returns the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.

import math
import re

def euler():
    """
    Find the unique positive integer n such that n^2 has the form
        1_2_3_4_5_6_7_8_9_0
    where each '_' is exactly one digit.
    """
    # Minimum and maximum 19-digit numbers matching pattern:
    MIN_SQUARE = 1020304050607080900
    MAX_SQUARE = 1929394959697989990

    # Compute integer square‐root bounds
    # The math.isqrt() method rounds a square root number downwards to the
    # nearest integer. Python >= 3.8 provides this method.
    # print (math.sqrt(25))  # 5.0
    # print (math.sqrt(30))  # 5.477225575051661
    # print (math.isqrt(25))  # 5
    # print (math.isqrt(30))  # 5
    low = math.isqrt(MIN_SQUARE)
    if low * low < MIN_SQUARE:
        low += 1
    high = math.isqrt(MAX_SQUARE)

    # n^2 must end in 0 -> n ends in 0
    # Round low up to next multiple of 10
    low += (10 - low % 10) % 10

    # Precompile a regex: 1.d2.d3.d4.d5.d6.d7.d8.d9.d0 for exactly 19 chars
    pattern = re.compile(r"^1\d2\d3\d4\d5\d6\d7\d8\d9\d0$")

    for n in range(low, high+1, 10):
        s = str(n * n)
        # Only 19‐digit squares can match
        if len(s) == 19 and pattern.match(s):
            return n

    raise ValueError("No solution found")

if __name__ == "__main__":
    result = euler()
    print(result)  # 1389019170
    # 1389019170^2 = 1929374254627488900
