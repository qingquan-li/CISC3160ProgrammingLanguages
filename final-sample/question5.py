"""
Write the following functions in Python using recursion.
No higher-order functions or list comprehensions can be used in the implementations.
1. my_zip(lst1, lst2): Let lst1 be [A1, A2, . . . , An], and lst2 be [B1, B2, . . . , Bn]. This function returns the association list [(A1, B1),(A2, B2), . . . ,(An, Bn)].
2. lookup(alist, x): This function returns the value associated with x in the association list alist. For example,
lookup([('a', 1), ('b', 2), ('c', 3)], 'b')
returns 2.
3. replicate(lst, n): This function replicates the elements of lst n times. For example
replicate(['a','b','c'],3)
returns ['a','a','a','b','b','b','c','c','c'].
"""

def my_zip(lst1, lst2):
    """
    Recursively zip two lists of equal length into an association list of pairs.
    """
    # Base case: if either list is empty, stop
    if not lst1 or not lst2:
        return []
    # Pair the heads, then recurse on the tails
    head_pair = (lst1[0], lst2[0])
    return [head_pair] + my_zip(lst1[1:], lst2[1:])

print(my_zip([1,2,3], ['a','b','c']))
# [(1, 'a'), (2, 'b'), (3, 'c')]


def my_zip_iteration(lst1, lst2):
    """
    Iteratively zip two lists into a list of pairs.
    """
    result = []
    # Only iterate up to the shorter length
    length = min(len(lst1), len(lst2))
    for i in range(length):
        # Pair element-by-element
        result.append((lst1[i], lst2[i]))
    return result

print(my_zip([1,2,3], ['a','b','c']))
# [(1, 'a'), (2, 'b'), (3, 'c')]


def lookup(alist, x):
    """
    Recursively search an association list for key x.
    Returns the corresponding value, or raises KeyError if not found.
    E.g. lookup([('a',1),('b',2)], 'b') → 2
    """
    # Base case: empty list → not found
    if not alist:
        raise KeyError(f"{x!r} not found")
    key, val = alist[0]
    if key == x:
        return val
    # Otherwise, search in the rest
    return lookup(alist[1:], x)

alist = [('a', 1), ('b', 2), ('c', 3)]
print(lookup(alist, 'b'))  # 2
try:
    lookup(alist, 'z')
except KeyError as e:
    print(e)  # "'z' not found"


def lookup_iteration(alist, x):
    """
    Iteratively search an association list for key x.
    """
    for key, val in alist:
        if key == x:
            return val
    # If we exit the loop, we never found x
    raise KeyError(f"{x!r} not found")

alist = [('a', 1), ('b', 2), ('c', 3)]
print(lookup_iteration(alist, 'b'))  # 2
try:
    lookup_iteration(alist, 'z')
except KeyError as e:
    print(e)  # "'z' not found"


def replicate(lst, n):
    """
    Recursively replicate each element of lst n times.
    E.g. replicate(['a','b'], 3) → ['a','a','a','b','b','b']
    """
    # Base cases:
    if n <= 0 or not lst:
        return []
    # Helper to replicate a single element x n times
    def replicate_one(x, count):
        if count <= 0:
            return []
        # prepend x and recurse
        return [x] + replicate_one(x, count - 1)

    # Replicate the head, then recurse on the tail
    head, *tail = lst
    return replicate_one(head, n) + replicate(tail, n)

print(replicate(['a','b','c'], 3))  # ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
print(replicate([1,2], 0))  # []


def replicate(lst, n):
    """
    Iteratively replicate each element of lst n times.
    """
    result = []
    # For each element in the input list...
    for x in lst:
        # ... append it n times
        for _ in range(n):
            result.append(x)
    return result

print(replicate(['a','b','c'], 3))  # ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
print(replicate([1,2], 0))  # []
