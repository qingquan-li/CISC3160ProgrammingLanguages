# replicate(lst,n): Replicate each of the elements of lst a given number of
# times. For example, for lst = [a,b,c] and n = 3, the returned list is
# [a,a,a,b,b,b,c,c,c].

def replicate(lst, n):
    result = []
    for i in lst:
        for _ in range(n):
            result.append(i)

    return result

# Example usage:
lst = ['a', 'b', 'c']
print(replicate(lst, 3))
