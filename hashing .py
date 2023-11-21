# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:36:08 2023

@author: SOHAIL MUHAMMAD
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # A simple hash function that takes the ASCII values of characters in the key
        # and calculates the hash code as the sum of these values
        hash_code = sum(ord(char) for char in key)
        return hash_code % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # If there's a collision, use chaining (linked list)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            # Check if the key already exists in the chain, and update the value
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    break
            else:
                # If the key doesn't exist in the chain, add a new key-value pair
                self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        # Search for the key in the chain
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        # If the key is not found
        raise KeyError(f"Key '{key}' not found in the hash table")

# Example usage:
hash_table = HashTable(size=10)
hash_table.insert("name", "John")
hash_table.insert("age", 25)
# hash_table.insert('name', 'Ali')
# hash_table.inssert('age', 35)
# Retrieving values
print("Name:", hash_table.get("name"))
print("Age:", hash_table.get("age"))
