# min_max_median(lst): a function that takes a simple list of numbers lst as a
# parameter and returns a list with the min, max, and the median of lst. Can
# you devise an algorithm that has an expected linear running time?

# Leetcode 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import random

# Helper function
def quickselect(a, k):
    """
    Return the k-th smallest element (0-based) from list a.
    Uses in-place Quickselect, so we work on a copy.
    Expected O(n) time.
    """
    arr = list(a)  # work on a copy
    def select(lo, hi, k):
        if lo == hi:
            return arr[lo]
        # pick a random pivot index
        p = random.randint(lo, hi)
        # partition around arr[p]
        pivot = arr[p]
        # move pivot to end
        arr[p], arr[hi] = arr[hi], arr[p]
        store = lo
        for i in range(lo, hi):
            if arr[i] < pivot:
                arr[store], arr[i] = arr[i], arr[store]
                store += 1
        # move pivot to its final place
        arr[store], arr[hi] = arr[hi], arr[store]
        # store is pivot index
        if k == store:
            return arr[store]
        elif k < store:
            return select(lo, store - 1, k)
        else:
            return select(store + 1, hi, k)
    return select(0, len(arr) - 1, k)

def min_max_median(lst):
    """
    Returns [min, max, median] of lst.
    Median is the middle element if len is odd,
    or the average of the two middle elements if even.
    Expected O(n) time.
    """
    n = len(lst)
    if n == 0:
        raise ValueError("List must be non-empty")

    # 1) Find min and max in one pass
    mn = mx = lst[0]
    for x in lst[1:]:
        if x < mn: mn = x
        if x > mx: mx = x

    # 2) Find median via Quickselect
    if n % 2 == 1:
        # odd: single middle element
        med = quickselect(lst, n // 2)
    else:
        # even: average of lower and upper middles
        m1 = quickselect(lst, n//2 - 1)
        m2 = quickselect(lst, n//2)
        med = (m1 + m2) / 2

    return [mn, mx, med]

# --- Example Usage ---
lst1 = [7, 2, 9, 4, 3, 8, 1]
print(min_max_median(lst1))  # [1, 9, 4]

lst2 = [5, 2, 1, 4]
print(min_max_median(lst2))  # [1, 5, 3.0]

lst3 = [10]
print(min_max_median(lst3))  # [10, 10, 10]
