# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:36:53 2023

@author: SOHAIL MUHAMMAD
"""
unordered_list = [10, 60, 20, 13, 100]

def search(unordered_list, term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:
            print('Searched value is available in the list')
            return i, term
    return None

S = search(unordered_list, 13)
print(f'The value {S[1]} is available in the unordered list at index {S[0]}')

def search1(ordered_list, term):
        ordered_list_size = len(ordered_list)
        for i in range(ordered_list_size):
            if term == ordered_list[i]:
                return i
            elif ordered_list[i] > term:
                return None
        return None
    
ordered_list = [1,2,3,4,5,6,7]
ss = search1(ordered_list, 5)
print(f'the searched value {ss} is avaliable')