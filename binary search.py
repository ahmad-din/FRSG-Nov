# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:21:43 2023

@author: SOHAIL MUHAMMAD
"""

def binary_search(ordered_list, term):
    low, high = 0, len(ordered_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if ordered_list[mid] == term:
            return mid  # Term found, return the index
        elif ordered_list[mid] < term:
            low = mid + 1
        else:
            high = mid - 1

    return None  # Term not found

ordered_list = [1, 2, 3, 4, 5, 6, 7]
result = binary_search(ordered_list, 7)
print(result)
if result is not None:
    print(f'The searched value {ordered_list[result]} is available at index {result}')
else:
    print(f'The searched value is not present in the ordered list')
