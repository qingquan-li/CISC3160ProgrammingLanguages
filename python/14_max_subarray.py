# max_subarray(arr): return a contiguous subarray within arr which has the
# largest sum.

# Leetcode 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

def max_subarray(arr):
    """
    Return the contiguous subarray of `arr` with the largest sum.
    If there are multiple with the same max sum, returns the leftmost one.
    Uses Kadane's algorithm in O(n) time.
    """
    if not arr:
        return []

    # current best ending here, and overall best
    current_sum = max_sum = arr[0]
    start = end = 0      # bounds of the overall best subarray
    temp_start = 0       # potential start for the current run

    for i in range(1, len(arr)):
        x = arr[i]
        # Should we start new at x, or extend the run?
        if current_sum + x < x:
            current_sum = x
            temp_start = i
        else:
            current_sum += x

        # Update overall best?
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    # slice from start through end inclusive
    return arr[start:end+1]


# Example Usage

arr1 = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(arr1))
# [4, -1, 2, 1]

arr2 = [1]
print(max_subarray(arr2))
# [1]

arr3 = [5,4,-1,7,8]
print(max_subarray(arr3))
# [5, 4, -1, 7, 8]

arr4 = []
print(max_subarray(arr4))
# []
