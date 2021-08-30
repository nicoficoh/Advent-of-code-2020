#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:29:37 2021

@author: nico
"""

f=open('list')
line= f.readlines()
rows,cols=[],[]
[rows.append(el[:7]) for el in line]
[cols.append(el.strip()[-3:]) for el in line] #with strip we remove the \n
start=0
end=127
n=128
rowid=[]
for row in rows:
    i=1
    d=2
    for let in row:
        if let=='B':
            start+=n/d #we are restricting the limit every step until the limit coincides with one exact number
        if let=='F':
            end-=n/d
            
        i+=1
        d=2**i  
    rowid.append(int(start)*8)    
    start=0
    end=127
    

colid=[]
n=8
for col in cols:
    i=1
    d=2
    for let in col:
        if let=='R':
            start+=n/d
        if let=='L':
            end-=n/d
            
        i+=1
        d=2**i     
    colid.append(int(start))        
    start=0
    end=8

#Zip creates tuples
ID= [x + y for x, y in zip(rowid,colid)] #ID is defined as the sum of colid and rowid

#sol1
print(max(ID))

#Pt2
ID=sorted(ID)
for i in range(len(ID)-1):
    if ID[i+1]- ID[i] != 1: #if these numbers are not consecutives
        print(ID[i+1], ID[i])
        
    




