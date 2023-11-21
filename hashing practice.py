# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:26:21 2023

@author: SOHAIL MUHAMMAD
"""
hash_table = [None] * 50
print(hash_table)

# def simple_hashing(key):
#     return key % len(hash_table)

# print(simple_hashing(12))
# print(simple_hashing(13))
# print(simple_hashing(12))

# def insert(table, key, value):
#     hk = simple_hashing(key)
#     table[hk] = value

# insert(hash_table, 12, 'pakistan')
# print(hash_table)


#hash_table = [None]*50
#print(hash_table)
hash_table = [[] for _ in range(20)]
print(hash_table)

def hashing(key):
    return key % len(hash_table)

hashing(12)
hashing(13)
hashing(12)


def insert(tab, key, value):
    hk = hashing(key)
    tab[hk] = value
    
insert(hash_table, 12, 'pakistan')
print(hash_table)