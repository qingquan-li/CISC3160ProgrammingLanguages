# split_list(lst,n): split lst into two parts with the first part having n
# elements, and return a list that contains these two parts.

def split_list(lst, n):
    first_part = lst[:n]
    second_part = lst[n:]
    return [first_part, second_part]

# Example useage:
print(split_list([1,2,3,4,5], 3))   # [[1, 2, 3], [4, 5]]
print(split_list([1,2,3], 0))   # [[], [1, 2, 3]]
print(split_list([1,2,3], 5))   # [[1, 2, 3], []]
print(split_list([], 10))   # [[], []]
