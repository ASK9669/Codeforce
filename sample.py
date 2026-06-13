#X. Two intervals
#Given two intervals, determine if they overlap. Intervals are represented as a pair of integers, where the first integer is the start of the interval and the second integer is the end of the interval.
def intervals_overlap(interval1, interval2):    # Check if the intervals overlap
    return interval1[0] < interval2[1] and interval1[1] > interval2[0]  # Example usage
interval1 = (1, 5)
interval2 = (3, 7)
print(intervals_overlap(interval1, interval2))  # Output: True
interval3 = (6, 8)
print(intervals_overlap(interval1, interval3))  # Output: False
