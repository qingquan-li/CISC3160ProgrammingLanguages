# split_list(lst,n): split lst into two parts with the first part having
# n elements, and return a list that contains these two parts.

function split_list(lst, n)
    len = length(lst)
    # Clamp n into the range 0…len
    if n < 0
        n1 = 0
    elseif n > len
        n1 = len
    else
        n1 = n
    end

    # lst[1:0] → empty, lst[len+1:end] → empty
    part1 = lst[1:n1]
    part2 = lst[n1+1:end]

    return [part1, part2]
end

# Examples
lst = ['a','b','c','d','e','f']

println(split_list(lst, 3))  # [['a','b','c'], ['d','e','f']]
println(split_list(lst, 0))  # [Char[], ['a', 'b', 'c', 'd', 'e', 'f']]
println(split_list(lst, 6))  # [['a', 'b', 'c', 'd', 'e', 'f'], Char[]]
println(split_list(lst, 10)) # [['a', 'b', 'c', 'd', 'e', 'f'], Char[]]
