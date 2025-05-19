# days(date1,date2): a function that takes two dates, date1 and date2, in some
# format, and returns the number of days from date1 to date2, inclusive.

# Leetcode 1360. Number of Days Between Two Dates
# https://leetcode.com/problems/number-of-days-between-two-dates/

from datetime import datetime

def daysBetweenDates(date1: str, date2: str) -> int:

        # Parse a string into a datetime object given a corresponding format
        # datetime.strptime(date_string, format)
        d1 = datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.strptime(date2, "%Y-%m-%d").date()
        return abs((d1 - d2).days) + 1


# Example usage:
print(daysBetweenDates("2019-06-29", "2019-06-30"))  # 2
print(daysBetweenDates("2020-01-15", "2019-12-31"))  # 16
