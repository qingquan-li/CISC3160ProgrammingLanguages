#=
Write each of the following pure functions on LinkedList.

1. Test if a list is sorted in ascending order.
2. Merge two sorted lists.
3. Test if a list is cyclic.
4. Remove duplicates from a sorted list.
5. Test if a list is palindromic.
=#


# A Simple Immutable LinkedList
# A LinkedList can be either Empty or a Cons(head, tail)
abstract type LinkedList{T} end

struct Empty{T} <: LinkedList{T} end
struct Cons{T}  <: LinkedList{T}
    head::T
    tail::LinkedList{T}
end

# A helper to build lists more easily:
cons(x, xs::LinkedList{T}) where T = Cons{T}(x, xs)

# Example:  list = cons(1, cons(2, cons(3, Empty{Int}())))


# A Mutable LinkedList Definition
# mutable struct ListNode
#     data
#     next::Union{ListNode, Nothing}
# end

# LinkedList = Union{ListNode, Nothing}


# 1. Test if a list is sorted in ascending order
function is_sorted(lst::LinkedList{T}) where T
    # Empty or single-element is sorted
    if lst isa Empty || (lst.tail isa Empty)
        return true
    end
    # Compare head to next head, then recurse
    if lst.head <= (lst.tail).head
        return is_sorted(lst.tail)
    else
        return false
    end
end


# 2. Merge two sorted lists.
function merge(l1::LinkedList{T}, l2::LinkedList{T}) where T
    if l1 isa Empty
        return l2
    elseif l2 isa Empty
        return l1
    elseif l1.head <= l2.head
        return cons(l1.head, merge(l1.tail, l2))
    else
        return cons(l2.head, merge(l1, l2.tail))
    end
end


# 3. Test if a list is cyclic.
function is_cyclic(lst::LinkedList)
    slow = lst
    fast = lst
    while (fast isa Cons) && (fast.tail isa Cons)
        slow = (slow::Cons).tail
        fast = (fast::Cons).tail.tail
        if slow === fast
            return true
        end
    end
    return false
end


# 4. Remove duplicates from a sorted list.
function remove_duplicates(lst::LinkedList{T}) where T
    if lst isa Empty
        return lst
    end
    # Recursively clean the tail
    let
        h = lst.head
        t = lst.tail
        cleaned_tail = remove_duplicates(t)
        # If head equals the next head, skip this element
        if (cleaned_tail isa Cons) && (h == (cleaned_tail::Cons).head)
            return cleaned_tail
        else
            return cons(h, cleaned_tail)
        end
    end
end


# 5. Test if a list is palindromic.
function is_palindromic(lst::LinkedList{T}) where T
    # Convert to a simple Array to compare front/back
    arr = []
    cur = lst
    while cur isa Cons
        push!(arr, (cur::Cons).head)
        cur = (cur::Cons).tail
    end
    # Check symmetry
    n = length(arr)
    for i in 1:div(n,2)
        if arr[i] != arr[n - i + 1]
            return false
        end
    end
    return true
end


# Example Usage

# Build a linked list: [1,1,2,3,3,3,4]
lst = cons(1, cons(1, cons(2, cons(3, cons(3, cons(3, cons(4, Empty{Int}())))))))

# 1. Test if a list is sorted in ascending order.
println("1. Sorted? ", is_sorted(lst))  # 1. Sorted? true

# 2. Merge two sorted lists.
sorted = cons(1, cons(2, cons(3, Empty{Int}())))
println("2. Merge: ", merge(sorted, cons(0, sorted)))
# 2. Merge: Cons{Int64}(0, Cons{Int64}(1, Cons{Int64}(1, Cons{Int64}(2, Cons{Int64}(2, Cons{Int64}(3, Cons{Int64}(3, Empty{Int64}())))))))

# 3. Test if a list is cyclic.
println("3. Cyclic? ", is_cyclic(lst))  # 3. Cyclic? false

# 4. Remove duplicates from a sorted list.
println("4. Deduped: ", remove_duplicates(lst))  # [1,2,3,4]
# 4. Deduped: Cons{Int64}(1, Cons{Int64}(2, Cons{Int64}(3, Cons{Int64}(4, Empty{Int64}()))))

# 5. Test if a list is palindromic.
pal = cons('a', cons('b', cons('b', cons('a', Empty{Char}()))))
println("5. Palindromic? ", is_palindromic(pal))  # 5. Palindromic? true
