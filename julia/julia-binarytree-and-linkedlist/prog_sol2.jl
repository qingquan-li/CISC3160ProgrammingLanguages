# Solutions from the professor.

mutable struct ListNode
    data
    next::Union{ListNode, Nothing}
end

LinkedList = Union{ListNode, Nothing}

# Test if a list is sorted in ascending order.
function is_sorted(lst::LinkedList)
    if lst === nothing || lst.next === nothing
        return true
    end
    return lst.data <= lst.next.data && is_sorted(lst.next)
end

# Merge two sorted lists.
function merge(lst1::LinkedList, lst2::LinkedList)
    if lst1 === nothing
        return lst2
    elseif lst2 === nothing
        return lst1
    elseif lst1.data <= lst2.data
        return ListNode(lst1.data, merge(lst1.next, lst2))
    else
        return ListNode(lst2.data, merge(lst1, lst2.next))
    end
end

# Test if a list is cyclic.
function is_cyclic(lst::LinkedList)
    slow = lst
    fast = lst

    while fast !== nothing && fast.next !== nothing
        slow = lst.next
        fast = lst.next.next
        if slow === fast
            return true
        end
    end
    return false
end


# Remove duplicates from a sorted list.
function remove_duplicates(lst::LinkedList)::LinkedList
    if lst === nothing || lst.next === nothing
        return lst
    elseif lst.data == lst.next.data
        return remove_duplicates(lst.next)
    else
        return ListNode(lst.data, remove_duplicates(lst.next))
    end
end

# Test if a list is palindromic.
function palindromic(head::LinkedList)
    v = list_to_vector(head)
    # return v == reverse(v)
    lo = 1
    hi = length(v)
    while (lo < hi)
        if (v[lo] != v[hi])
            return false
        end
        lo += 1
        hi -= 1
    end
    return true
end

mutable struct BNode
    data::Int
    left::Union{Nothing, BNode}
    right::Union{Nothing, BNode}
end

BTree = Union{Nothing, BNode}

# Return the in-order traversal of a tree as a list.
function inorder(r::BTree)
    visited = Vector{Int}()
    inorder(r, visited)
    return visited
end

function inorder(r::BTree, result::Vector{Int})
    if r === nothing
        return
    end
    inorder(r.left, result)
    push!(result, r.data)
    inorder(r.right, result)
end

# Test if a binary tree is symmetric 
function is_symmetric(root::BTree)::Bool 
    if root === nothing
        return true 
    end 
    return is_mirror(root.left, root.right) 
end 

function is_mirror(left::BTree, right::BTree)::Bool 
    if left === nothing && right === nothing 
        return true 
    elseif left === nothing || right === nothing 
        return false 
    else
        return (left.val == right.val) && 
                is_mirror(left.left, right.right) && 
                is_mirror(left.right, right.left) 
    end 
end

# Return the maximum path sum (the sum of the path from the root to a leaf is the sum of values in the nodes on the path).
function max_path_sum(root::BRoot)::Int
    if root === nothing 
        return 0
    else
        return root.data + max(max_path_sum(root.left), max_path_sum(root.right))
    end
end


# Test if a binary root is a search root.
function bst(root::BTree)
    if (root == nothing)
        return true
    else
        return bst(root, typemin(Int), typemax(Int))
    end
end

function bst(root::BTree, lb, ub)
    if (root == nothing)
        return true
    else
        return lb <= root.data <= ub &&
            bst(root.left, lb, root.data) &&
            bst(root.right, root.data, ub)
    end
end


# Insert a value into a binary search tree such that the resulting tree remains a search tree.
function insertValue(root::BTree, value)::BTree
    if root === nothing
        return BTree(value, nothing, nothing)
    elseif value < root.data
        root.left = insertValue(root.left, value)
    elseif value > root.data
        root.right = insertValue(root.right, value)
    end
end

