function my_reduce(f, arr)
    # Check that the array is not empty.
    if isempty(arr)
        error("my_reduce requires a non-empty array")
    end

    # Start with the first element of the array.
    result = arr[1]
    
    # Iterate over the rest of the elements.
    for i in 2:length(arr)
        result = f(result, arr[i])
    end
    
    return result
end

# Example usage:
println("Sum: ", my_reduce(+, [1, 2, 3]))   # Expected output: 6
println("Product: ", my_reduce(*, [1, 2, 3])) # Expected output: 6
