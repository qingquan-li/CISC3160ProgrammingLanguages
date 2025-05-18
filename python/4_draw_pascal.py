# draw_pascal(N): a function that takes an integer N as a parameter and prints
# the first N rows of the Pascal's triangle.

# Leetcode Pascal's Triangle: https://leetcode.com/problems/pascals-triangle/

def draw_pascal(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    # if numRows > 2
    pascal_triangle = [[1], [1, 1]]

    for current_row in range(1, numRows - 1):  # range(1, 4)
        next_row_array = []
        for index in range(current_row + 1):  # range(2)
            if index == 0:
                next_row_array.append(1)
            else:
                next_row_array.append(pascal_triangle[current_row][index-1] + pascal_triangle[current_row][index])
        next_row_array.append(1)  # Add 1 to the end
        pascal_triangle.append(next_row_array)

    return pascal_triangle


# Example usage:
print(draw_pascal(5))
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1