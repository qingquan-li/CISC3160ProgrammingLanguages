# remove_consecutive_dups(lst): return a copy of lst with consecutive duplicates of elements eliminated. For example, for lst = [a,a,a,a,b,c,c,a,a,d,e,e,e,e],
# the returned list is [a,b,c,a,d,e].

function remove_consecutive_dups(lst)
    n = length(lst)
    n == 0 && return []           # empty input → empty output

    # start the result with the first element
    result = [lst[1]]

    # walk the rest of lst
    for i in 2:n
        if lst[i] != lst[i-1]
            push!(result, lst[i])
        end
    end

    return result
end

# Example usage:
lst = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
println(remove_consecutive_dups(lst))  # ['a', 'b', 'c', 'a', 'd', 'e']

# Works for numbers too:
nums = [1,1,2,2,2,3,3,1,1,0,0]
println(remove_consecutive_dups(nums))  # [1, 2, 3, 1, 0]
