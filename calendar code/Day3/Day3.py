#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:09:08 2021

@author: nico
"""

f=open('list')
#Attention with f.readline() cauese often \n is included, .strip() is necessary
#every row included 31 signs, so max position is 30
l=[]
for el in f:
    l.append(el)

def doit(n,m):
    pos=0
    alberi=0
    for el in l:
        if pos >=(30-n): #if we are approacing the border of the row we have to initialize the new line-
    
            print(pos,el[pos])
            if el[pos]=='#':
                alberi+=1
            pos-=(30-n)
        else:
            print(pos,el[pos])
            if el[pos]=='#':
                alberi+=1
            pos+=m
    print(alberi)

#1D1R
#doit(0,1)
#53

#1D3R
#doit(2,3) 
#167

#1D5R
#doit(4,5)
#54

#1D7R
#doit(6,7)
#67

#2D1R
 
def fdoit():
    pos=0
    alberi=0   
    for i in range(0, len(l), 2): #step of 2, the plain is going down of 2 rows
            if pos >=30:
                print(pos,l[i][pos])
                if l[i][pos]=='#':
                    alberi+=1
                pos-=30
            else:
                print(pos,l[i][pos])
                if l[i][pos]=='#':
                    alberi+=1
                pos+=1
    print(alberi)
#fdoit()
#23

result= 23*67*54*167*53

