#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:41:19 2021

@author: nicoficoh
"""

f= open('list')
l=[]
for el in f:
    l.append(str(el))
    
    
met=[]
pas=[]
for el in l:
    met.append(el.split(':')[0])
    pas.append(el.split(':')[1][:-1])   
     
    
num,lett=[],[]
for el in met:
    num.append(el.split(' ')[0])
    lett.append(el.split(' ')[1])
    
mini,maxi=[],[]   
for num in num:
    mini.append(int(num.split('-')[0])-1)
    maxi.append(int(num.split('-')[1])+1)
    

s=0        
for i in range(len(pas)):
    if pas[i].count(lett[i])>mini[i] and pas[i].count(lett[i])<maxi[i]:
        s+=1

s=0   
#PART TWO  
for i in range(len(pas)):
    if pas[i][mini[i]-1]==lett[i] or pas[i][maxi[i]-1]==lett[i]:
        s+=1
print(s)
        
        

        
