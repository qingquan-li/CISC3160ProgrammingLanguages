# max_subarray(arr): return a contiguous subarray within arr which has the largest sum.

# Uses Kadane's algorithm in O(n) time.
function max_subarray(arr)
    n = length(arr)
    n == 0 && return []  # empty input → empty output

    # Initialize with the first element
    max_sum = arr[1]
    current_sum = arr[1]
    max_start = 1
    max_end = 1
    current_start = 1

    for i in 2:n
        x = arr[i]
        # If starting new subarray at i is better than extending
        if current_sum + x < x
            current_sum = x
            current_start = i
        else
            current_sum += x
        end

        # Check if the current subarray is the best so far
        if current_sum > max_sum
            max_sum   = current_sum
            max_start = current_start
            max_end   = i
        end
    end

    return arr[max_start:max_end]
end

# Example usage:
println(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  
# [4, -1, 2, 1]

println(max_subarray([-5, -1, -8]))  
# [-1]
