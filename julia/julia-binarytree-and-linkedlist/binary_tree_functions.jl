#=
Write each of the following functions on a binary tree with a given root of the type BTree.

1. Return the in-order traversal of a tree as a list.
2. Test if a binary tree is symmetric (a binary tree is symmetric if rotating it about the vertical bar through the root for 180 degrees gives the same tree).
3. Return the maximum path sum (the sum of the path from the root to a leaf is the sum of values in the nodes on the path).
4. Test if a binary tree is a search tree.
5. Test if a given value occurs in a binary search tree.
6. Insert a value into a binary search tree such that the resulting tree remains a search tree.
=#


# Define the BTree type

abstract type BTree{T} end
struct Empty{T} <: BTree{T} end
struct Node{T}  <: BTree{T}
    val::T
    left::BTree{T}
    right::BTree{T}
end


# 1. Return the in-order traversal of a tree as a list.
function inorder(tree::BTree{T}) where T
    if tree isa Empty
        return Vector{T}()  # empty list
    end
    # tree is a Node
    n = tree
    left_list  = inorder(n.left)
    push!(left_list, n.val)
    right_list = inorder(n.right)
    append!(left_list, right_list)
    return left_list
end


# 2. Test if a binary tree is symmetric
function is_symmetric(tree::BTree{T}) where T
    tree isa Empty && return true
    n = tree
    return _is_mirror(n.left, n.right)
end

function _is_mirror(a::BTree{T}, b::BTree{T}) where T
    if a isa Empty && b isa Empty
        return true
    elseif (a isa Empty) || (b isa Empty)
        return false
    else
        na, nb = a, b
        return na.val == nb.val &&
               _is_mirror(na.left,  nb.right) &&
               _is_mirror(na.right, nb.left)
    end
end


# 3. Return the maximum path sum
function max_path_sum(tree::BTree{T}) where T<:Number
    if tree isa Empty
        return zero(T)
    end
    n = tree
    # if only one child exists, go that way
    if n.left isa Empty && n.right isa Empty
        return n.val
    elseif n.left isa Empty
        return n.val + max_path_sum(n.right)
    elseif n.right isa Empty
        return n.val + max_path_sum(n.left)
    else
        return n.val + max(max_path_sum(n.left),
                            max_path_sum(n.right))
    end
end


# 4. Test if a binary tree is a search tree.
function is_search_tree(tree::BTree{T}) where T<:Real
    arr = inorder(tree)
    for i in 1:length(arr)-1
        if arr[i] > arr[i+1]
            return false
        end
    end
    return true
end


# 5. Test if a given value occurs in a binary search tree.
function occurs(tree::BTree{T}, x::T) where T
    if tree isa Empty
        return false
    end
    n = tree
    if x == n.val
        return true
    elseif x < n.val
        return occurs(n.left, x)
    else
        return occurs(n.right, x)
    end
end


# 6. Insert a value into a binary search tree such that the resulting tree remains a search tree.
function insert(tree::BTree{T}, x::T) where T
    if tree isa Empty
        return Node(x, Empty{T}(), Empty{T}())
    end
    n = tree
    if x < n.val
        return Node(n.val, insert(n.left, x), n.right)
    elseif x > n.val
        return Node(n.val, n.left, insert(n.right, x))
    else
        return tree   # no duplicates
    end
end


# Example Usage

# === Build a binary tree ===
#        5
#       / \
#      3   7
#     /   / \
#    2   6   9

t = Node(5,
        Node(3,
             Node(2, Empty{Int}(), Empty{Int}()),
             Empty{Int}()),
        Node(7,
             Node(6, Empty{Int}(), Empty{Int}()),
             Node(9, Empty{Int}(), Empty{Int}())))

# 1. Return the in-order traversal of a tree as a list.
println("1. In-order: ", inorder(t))
# 1. In-order: [2, 3, 5, 6, 7, 9]

# 2. Test if a binary tree is symmetric
println("2. Symmetric? ", is_symmetric(t))
# 2. Symmetric? false

# 3. Return the maximum path sum
println("3. Max path sum: ", max_path_sum(t))
# Paths: 5→3→2 sum=10, 5→7→6 sum=18, 5→7→9 sum=21
# 3. Max path sum: 21

# 4. Test if a binary tree is a search tree.
println("4. BST? ", is_search_tree(t))
# 4. BST? true

# 5. Test if a given value occurs in a binary search tree.
println("5. Occurs 6? ", occurs(t, 6))
# 5. Occurs 6? true

# 6. Insert a value into a binary search tree such that the resulting tree remains a search tree.
u = insert(t, 4)
println("6. After insert 4, in-order: ", inorder(u))
# After insert 4, in-order: [2, 3, 4, 5, 6, 7, 9]
