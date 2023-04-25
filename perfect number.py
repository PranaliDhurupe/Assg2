# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:36:04 2022

@author: Pranali
"""

n = int(input())
arr = []
for i in range(1,n):
    if n % i == 0:
        arr.append(i)
if sum(arr) == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")