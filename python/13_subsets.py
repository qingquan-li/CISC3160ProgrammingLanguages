# subsets(s,n): return the set of n-element subsets of s.

# Leetcode 77. Combinations
# https://leetcode.com/problems/combinations/

def subsets(s, n):
    """
    Return a list of all n-element subsets of the list s.
    Each subset is a list; order of subsets does not matter.
    """
    # Base cases:
    if n == 0:
        return [[]]
    if n > len(s):
        return []

    head, tail = s[0], s[1:]

    # 1) Build all subsets that include `head`
    with_head = []
    # We need all (n-1)-element subsets of tail,
    # then for each one, prepend head.
    for comb in subsets(tail, n-1):
        # comb is one of the (n-1)-element subsets from tail
        new_subset = [head] + comb
        with_head.append(new_subset)
        # e.g. if head = 'a' and comb = ['c','d'], new_subset = ['a','c','d']

    # 2) Build all subsets that exclude `head`
    without_head = subsets(tail, n)

    # 3) Combine and return
    return with_head + without_head


# Example usage:
if __name__ == "__main__":
    s = ['a','b','c','d']
    print(subsets(s, 2))
    # [['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd']]

    print(subsets([1,2,3,4], 3))
    # [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
