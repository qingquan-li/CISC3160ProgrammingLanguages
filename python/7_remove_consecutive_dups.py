# remove_consecutive_dups(lst): return a copy of lst with consecutive
# duplicates of elements eliminated. For example, for
# lst = [a,a,a,a,b,c,c,a,a,d,e,e,e,e], the returned list is [a,b,c,a,d,e].

# Leetcode 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


def remove_consecutive_dups(lst):
    stack = []

    for i in lst:
        if stack and i == stack[-1]:
            stack.pop()
        stack.append(i)

    return stack

# Example usage:
lst = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
print(remove_consecutive_dups(lst))
# ['a', 'b', 'c', 'a', 'd', 'e']