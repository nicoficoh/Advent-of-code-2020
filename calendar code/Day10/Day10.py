#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:07:34 2021

@author: nico
"""

l=[]
with open("/home/nico/Desktop/calendar code/Day10/list", "r") as fp:
    for el in fp:
        l.append(int(el.strip()))
l = [0] + l
l.append(max(l)+3)       
l=sorted(l)


one, three= [],[]
for i in range(len(l)-1):
    if l[i+1]-l[i]==1:
        one.append('one')
    else:
        three.append('three')
        #I add either to one and three 1 values cause it's from 0->1 and from max->max+3

#Sol pt1   
#print((len (one))*(len(three)))

#Pt2

checked = {}

#Recursive function
def funzione(pos):
    if pos == len(l)-1:
        return 1 #there's only one way to go from the second to last to the last one
        
    if pos in checked:
        #print(pos)
        #print(checked[pos]) #value è il valore di differenza
        return checked[pos]
         

    total = 0
    for i in range(pos+1, len(l)):
        print(i)
        if l[i] - l[pos] <= 3:
            total += funzione(i)

    checked[pos] = total
    return total

print(funzione(0)) #si parte con pos=0!


from collections import defaultdict
counts = defaultdict(int, {0: 1})
diffs = defaultdict(int)


for a, b in zip(l[1:], l): #Cute way to solve pt1
    diffs[a - b] += 1
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]
    
    
