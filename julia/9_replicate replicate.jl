# replicate(lst,n): Replicate each of the elements of lst a given number of times.
# For example, for lst = [a,b,c] and n = 3, the returned list is [a,a,a,b,b,b,c,c,c].

function replicate(lst, n)
    result = []                # start with an empty array
    for x in lst
        for i in 1:n
            push!(result, x)
        end
    end
    return result
end

# Example usage:
lst = ['a','b','c']
println(replicate(lst, 3))   # Any['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']

nums = [1, 2, 3]
println(replicate(nums, 2))  # Any[1, 1, 2, 2, 3, 3]