#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:51:11 2021

@author: nico
"""
f=open('/home/nico/Desktop/calendar code/Day6/list')

s=''
for el in f:
    s+=el
lista=s.strip().split('\n\n')

l=[]
for el in lista:
    l.append(el.split('\n'))
s=0
gruppo=[]
for el in l:
    gruppo=[]
    for el in el:        
        for i in el:
            if not i in gruppo:# if the element is the distinct
#(first time seen) I put it into a list and then all together count)
                gruppo.append(i)
    s+=(len(gruppo))       
#print(s)


#PART TWO

s=0
for el in l:
    if len(el)==1: #If the group contain 1 person,
                    #all the question are valid
        for el1 in el:
            s+=(len(el1))
    else:        
        gruppo=[]
        for el1 in el:
            for i in el1:# All the element of the group inside a list
                        #only the repetuted in all the people are taken
                gruppo.append(i)
        #Set is taking only the repetuted element
        s+=len((set(i for i in gruppo if gruppo.count(i) == len(el))))
print(s)
  

              
            
            
            
            