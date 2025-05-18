# bc(n,k): return the binomial coefficient "n choose k". Can you figure out
# a method that is less likely to cause an overflow than using the formula
# (n*(n-1)*...*(n-k+1))/(k*(k-1)*...*2)?

"""
    bc(n, k)

Compute the binomial coefficient “n choose k” in O(min(k, n-k)) time,
using an algorithm that keeps the intermediate values small by
dividing at each step.

Returns 0 if k < 0 or k > n.
"""
function bc(n::Integer, k::Integer)
    # Handle out-of-range cases
    if k < 0 || k > n
        return 0
    end
    # Use symmetry: C(n,k) == C(n, n−k)
    k = min(k, n - k)
    result = one(n)  # start with 1, same type as n
    for i in 1:k
        # Multiply by the next factor in the numerator,
        # then divide by i (exactly) to keep numbers small
        result = result * (n - k + i) ÷ i
    end
    return result
end

# Example usage:
println(bc(5, 2))   # 10
println(bc(10, 3))  # 120
println(bc(30,15))  # 155117520
