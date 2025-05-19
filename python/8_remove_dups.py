# remove_dups(lst): return a copy of lst with duplicates of elements
# eliminated. For example, for lst = [a,a,a,a,b,c,c,a,a,d,e,e,e,e],
# the returned list is [a,b,c,d,e].

def remove_dups(lst):
    # result = list(set(lst))
    # result.sort()
    # return result
    # If you used set(lst) you’d lose all ordering (sets are unordered)
    # lst = ['b','a','c','b'] => return ['a', 'b', 'c'] instead of ['b','a','c']

    result = []
    seen = set()

    for i in lst:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result

# Example usage:
lst = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
print(remove_dups(lst))
# ['a', 'b', 'c', 'd', 'e']
