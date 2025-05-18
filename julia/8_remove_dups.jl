# remove_dups(lst): return a copy of lst with duplicates of elements eliminated.
# For example, for lst = [a,a,a,a,b,c,c,a,a,d,e,e,e,e], the returned list is [a,b,c,d,e].

function remove_dups(lst)
    result = []                # start with an empty array
    for x in lst
        # only add x if we haven't seen it in result yet
        if !(x in result)
            push!(result, x)
        end
    end
    return result
end

# Example usage:
lst = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
println(remove_dups(lst))    # Any['a', 'b', 'c', 'd', 'e']

nums = [1,2,1,3,2,4,3,5]
println(remove_dups(nums))   # Any[1, 2, 3, 4, 5]
