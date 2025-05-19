# bc(n,k): return the binomial coefficient "n choose k". Can you figure out a
# method that is less likely to cause an overflow than using the formula
# (n*(n-1)*...*(n-k+1))/(k*(k-1)*...*2)?

def bc(n, k):
    """
    Compute the binomial coefficient “n choose k” in O(min(k, n-k)) time,
    avoiding large intermediate factorials by dividing at each step.

    Returns 0 if k < 0 or k > n.
    """
    # Out‐of‐range
    if k < 0 or k > n:
        return 0
    # symmetry: C(n,k) == C(n, n-k)
    k = min(k, n - k)
    result = 1
    # multiply by (n-k+1) ... n, dividing by 1 ... k as we go
    for i in range(1, k+1):
        result = result * (n - k + i) // i
    return result

# Example usage
if __name__ == "__main__":
    print(bc(5, 2))    # 10
    print(bc(10, 3))   # 120
    print(bc(30,15))   # 155117520
    print(bc(5, 6))    # 0
