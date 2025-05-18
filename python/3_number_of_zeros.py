# number_of_zeros(Lst): a function that returns the number of zeros in a given
# simple list of numbers Lst.

def number_of_zeros(Lst):
    # return Lst.count(0)
    count = 0
    for i in Lst:
        if i == 0:
            count += 1
    return count

# Example usage:
print(number_of_zeros([0, 1, 2, 0, 3, 0]))  # 3
