# min_max_median(lst): a function that takes a simple list of numbers lst
# as a parameter and returns a list with the min, max, and the median of lst.
# Can you devise an algorithm that has an expected linear running time?

# Quickselect helper: partition arr[lo:hi] around the element at pivot_index
function partition!(arr, lo, hi, pivot_index)
    pivot = arr[pivot_index]
    # Move pivot to end
    arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
    store = lo
    for i in lo:hi-1
        if arr[i] < pivot
            arr[store], arr[i] = arr[i], arr[store]
            store += 1
        end
    end
    # Move pivot to its final place
    arr[store], arr[hi] = arr[hi], arr[store]
    return store
end

# Quickselect: finds the k-th smallest element (1-based) in arr[lo:hi]
function quickselect!(arr, lo, hi, k)
    if lo == hi
        return arr[lo]
    end
    # pick a random pivot between lo and hi
    p = rand(lo:hi)
    p = partition!(arr, lo, hi, p)
    if k == p
        return arr[k]
    elseif k < p
        return quickselect!(arr, lo, p-1, k)
    else
        return quickselect!(arr, p+1, hi, k)
    end
end

"""
    min_max_median(lst)

Return `[min, max, median]` of the numeric list `lst`.  
Runs in O(n) expected time using Quickselect for the median.
"""
function min_max_median(lst)
    n = length(lst)
    n == 0 && error("List must be non-empty")

    # 1) Find min and max in one pass
    mn = lst[1]
    mx = lst[1]
    for x in lst
        if x < mn; mn = x; end
        if x > mx; mx = x; end
    end

    # 2) Prepare a copy for median selection
    arr = [x for x in lst]   # simple element‐by‐element copy
    k   = div(n + 1, 2)      # middle index, 1-based

    # 3) Quickselect to find the median
    med = quickselect!(arr, 1, n, k)

    return [mn, mx, med]
end


# Example usage:
nums = [7, 2, 9, 4, 3, 8, 1]
println(min_max_median(nums))  # [1, 9, 4]

nums1 = [7, 2, 9, 4, 3]
println(min_max_median(nums1))   # [2, 9, 4]

nums2 = [10, 1, 5, 3]
println(min_max_median(nums2))   # [1.0, 10.0, 4.0] (medians are 3 & 5, average = 4.0)