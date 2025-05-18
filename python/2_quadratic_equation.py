# quadratic_equation(A,B,C): a function that computes the real roots of a
# given quadratic equation A*X^2+B*X+C=0.

import math

def quadratic_equation(a, b, c):
    """
    Compute the real roots of a*x^2 + b*x + c = 0.
    Returns a list of zero, one, or two real roots.
    """
    # Degenerate case: not actually quadratic
    if a == 0:
        if b == 0:
            return []             # no equation or infinite solutions—treat as “no real roots”
        return [-c / b]           # linear solution

    # Quadratic case
    disc = b*b - 4*a*c  # calculate the discriminant
    if disc < 0:
        return []                 # no real roots
    elif disc == 0:
        return [-b / (2*a)]      # one real (double) root
    else:
        sqrt_disc = math.sqrt(disc)
        return [(-b + sqrt_disc)/(2*a), (-b - sqrt_disc)/(2*a)]

# Example usage:
print(quadratic_equation(1, -3, 2))  # [2.0, 1.0]
print(quadratic_equation(1, 2, 1))  # [-1.0]
print(quadratic_equation(1, 0, -4))  # [2.0, -2.0]
print(quadratic_equation(0, 2, 1))  # [-0.5]
print(quadratic_equation(0, 0, 1))  # []