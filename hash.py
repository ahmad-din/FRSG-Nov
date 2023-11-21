# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:10:36 2023

@author: SOHAIL MUHAMMAD
"""
#https://www.youtube.com/watch?v=APAbRkrqDVI
import pandas as pd
mydict = {'ali':'01','shah':'02'}
#print(mydict)

my_dict = {'stdid':{'ali': {'id':'01', 'marks':'63'},
           'shah':{'id':'02','marks':'60'},'saim':{'id':'03', 'marks':'54'},'shah':{'id':'07','marks':'60'}}}
print(my_dict)

# print(mydict['ali'])
# # print(mydict.keys())
# # print(mydict.values())
# # print(my_dict.get('shah'))
# # print(my_dict.keys())
# # print(my_dict.values())
# for x in my_dict.keys():
#     print(x)
    
# for x,y in mydict.items():
#     print(x,y)
    
mydict['saim'] = '02'
#del mydict['ali']
# print(mydict.pop('saim'))
print(mydict)

dataframe = pd.DataFrame(my_dict['stdid'])
print(dataframe)

for value in mydict:
    print(value)
print(mydict['ali'])