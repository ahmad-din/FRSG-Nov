# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:28:56 2023

@author: SOHAIL MUHAMMAD
"""
# in this function we are passing the argument by value in line 11 we have assign value to x and when we call the function it copies the 
#value of the x and the result doesn't affect the original value of a
def ftn(a):
    sq_a = a**2
    return sq_a
a = 3
result = ftn(a)
print(result)



# In the following function the pass by reference method has followed, pass by reference means that when we make any changes 
# then all the changes occur in original value 

l = [1,2,3,4,5]
def fun(a):
    a[3] = 3**2
    return a
fun(l)
print(l)

# here we can see that when we make changes in 'a' the list l automatically changed