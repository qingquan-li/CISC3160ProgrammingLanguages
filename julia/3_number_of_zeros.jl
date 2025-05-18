# number_of_zeros(lst): a function that returns the number of zeros in a given
# simple list of numbers lst.

function number_of_zeros(lst)
    # Initialize a counter for zeros
    count = 0
    
    # Iterate through the list and count zeros
    for num in lst
        if num == 0
            count += 1
        end
    end
    
    return count
    
end

# Example usage:
lst = [0, 1, 2, 0, 3, 0, 4]
zeros_count = number_of_zeros(lst)
println("Number of zeros in the list: $zeros_count")
# Number of zeros in the list: 3