# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:09:24 2022

@author: Pranali
"""

def power(base,exp):
    if exp == 0:
        return 1
    else:
        return(base * power(base, exp-1))
    
print(power(2,2))