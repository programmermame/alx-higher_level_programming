#!/usr/bin/python3
"""
Find Peak task 6
"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the middle element is a peak
        if mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]:
            if mid == len(list_of_integers) - 1 or list_of_integers[mid] > list_of_integers[mid + 1]:
                return list_of_integers[mid]
            else:
                low = mid + 1
        else:
            high = mid - 1

    return None  # If no peak is found

