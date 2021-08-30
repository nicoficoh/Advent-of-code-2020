#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:41:19 2021

@author: nico
"""

f= open('list')
l=[]
for el in f:
    l.append(int(el))

    
for i in range(len(l)):
    for el in range(len(l)):
        for el1 in range(len(l)):
            
            somm=l[i]+l[el]+l[el1]
            if somm==2020:
                num1=l[i]
                num2=l[el]
                num3=l[el1]
            
print(num1, num2,num3)
print(num1*num2*num3)
