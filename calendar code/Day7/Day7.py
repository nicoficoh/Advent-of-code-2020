#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:08:25 2021

@author: nicoficoh
"""
import re
pattern=re.compile(r'\d\D')

with open("/home/nico/Desktop/calendar code/Day7/list", "r") as fp:
    lines=fp.readlines()

# We invert the lines: the bag that contain now it is contained
diz={}
def parseLine():
    for line in lines:
        child=[]
        diz1={}
        
        for i  in range(len(pattern.split(line))):        
            if (len(pattern.split(line)))==1:
                continue        
            if i==0:
                parent=(' '.join(pattern.split(line)[i].split(' ')[0:2]))
            else:
                child.append(' '.join(pattern.split(line)[i].split(' ')[0:2]))
                
            if not parent in diz:
                diz[parent]=child
    for k,v in diz.items():
        child= ' , '.join(v)
        if not k in diz1:
            diz1[k]=child

    return diz1


diz= parseLine()



# Part 1


def parentbag(childbag):                # function to find what bags can hold the childbag
                                         # iterate through the different bags
                                        # what bags can be in parent bag
    for parent,child in diz.items():
        
        if childbag in child:  
            print(childbag,child) # if the requested bag can be in parent bag
            parentbag(parent)
            # recursion to see what bag can hold the parent bag
            bagset.add(parent)          # add bag to set of bags allowed to (eventually) hold childbag
    return




bagset = set()
parentbag("shiny gold")
print("Part 1: The amount of different coloured bags that can hold a shiny gold bag: " + str(len(bagset)))
        
    



def add_child(parent_bag):
    # Function that will find the amount of individual bags insied a parent bag.
    # The function will go through the children of the parent bag to get their content
    # as well.
    content = diz[parent_bag].split(", ")
    if content[0] == "no other":
        return
    else:
        for child in content:           # iterate through the bags inside the parent bag
            bagname = child[2:]         # Bag name is second char onwards
            number = int(child[0])      # number of bags is the first (0th) char
            if bagname in children_counting:            # TRUE if bag has been counted already
                children_counting[bagname] += number    # increase the amount of that bag
            else:                                       # used if the bag has not been counted already
                children_counting[bagname] = number     # if the bag has not been counted already, add the number of it
            for i in range(number):     # iterate through the amount of bags
                add_child(bagname)      # go through each of the child bags inside the parent bag and get their content
        return


children_counting = {}
add_child("shiny gold")
print("Part 2: Total number of bags: " + str(sum(children_counting.values())))

                