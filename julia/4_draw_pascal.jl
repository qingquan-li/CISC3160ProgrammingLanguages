# draw_pascal(n): a function that takes an integer n as a parameter and prints
# the first n rows of the Pascal's triangle.

function draw_pascal(n)
    # Check if n is a positive integer
    if n < 1 || n != floor(n)
        error("n must be a positive integer.")
    end

    # Initialize the first row of Pascal's triangle
    pascal_triangle = [[1]]

    # Generate Pascal's triangle
    for i in 2:n  # Start from the second row
        new_row = [1]  # Start with 1
        for j in 2:i-1  # 2nd to i-1 (inclusive). Fill the middle values
            new_row = push!(new_row, pascal_triangle[i-1][j-1]
                            + pascal_triangle[i-1][j])
        end
        push!(new_row, 1)  # End with 1
        push!(pascal_triangle, new_row)
    end

    # Print the triangle
    for row in pascal_triangle
        println(join(row, " "))
    end
end

# Example usage:
n = 5
draw_pascal(n)
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1