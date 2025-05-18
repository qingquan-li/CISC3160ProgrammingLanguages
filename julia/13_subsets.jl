# subsets(s,n): return the set of n-element subsets of s.

function subsets(s, n)
    # Base cases
    n == 0 && return [ [] ]           # one subset: the empty one
    n > length(s) && return []        # no way to pick n > |s|

    # Split off the first element
    head, tail = s[1], s[2:end]

    # 1) All subsets that include head: pick (n-1) from tail and prepend head
    with_head = []
    for sub in subsets(tail, n-1)
        push!(with_head, [head; sub])   # [head; sub] concatenates head in front
    end

    # 2) All subsets that exclude head: pick n from tail
    without = subsets(tail, n)

    # 3) Combine and return
    result = copy(with_head)
    for sub in without
        push!(result, sub)
    end
    return result
end

# Example
s = ['a','b','c','d']
println(subsets(s, 2))
# Any[Any['a', 'b'], Any['a', 'c'], Any['a', 'd'], Any['b', 'c'], Any['b', 'd'], Any['c', 'd']]