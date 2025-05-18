# days(date1,date2): a function that takes two dates, date1 and date2,
# in some format, and returns the number of days from date1 to date2, inclusive.

using Dates

"""
    days(d1::Date, d2::Date) -> Int

Returns the number of days from d1 to d2 inclusive.
"""
function days(d1::Date, d2::Date)
    # Compute the absolute difference in days
    diff = abs(d2 - d1).value
    return diff + 1
end

# Example usage:
d1 = Date(2025, 4, 20)
d2 = Date(2025, 4, 22)
println(days(d1, d2))  # prints 3  (20th,21st,22nd)
