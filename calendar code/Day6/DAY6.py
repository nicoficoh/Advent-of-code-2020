#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:49:08 2021

@author: nico
"""

with open("/home/nico/Desktop/calendar code/Day6/list", "r") as fp:
    lines=fp.readlines()
    
groups = []
group = []
for question in lines:
    if question!="\n":#se non incomincia con un vuoto,
    #allora ha testo quindi splitti (si poteva anche usare strip)
    #e la metti dentro al gruppo
        group.append(question.split("\n")[0])
    else:#se invece ha il vuoto prendi il gruppo precedentemente formato
    #e appendi a gruppI
        groups.append(group)
        group=[]#poi inizializzi gruppo
groups.append(group)

solution_1 = []
for group in groups:
    #print(f"Group: ", group)
    unique_ques = []
    for ques in group:
        unique_ques.extend([uq for uq in ques])

    #print(f"Unique questions: {set(unique_ques)}")
    solution_1.extend(list(set(unique_ques)))
print(f"Solution 1: {len(solution_1)}")


from collections import Counter
total = 0
for group in groups:
    #print(f"\nGroup: {group}")
    group_size = len(group)
    #print(f"Length of group: {group_size}")

    # make single list of an entire group and count occurence
    counts = Counter("".join(group))
    print(Counter(list(counts.values()))[group_size])
    #print(counts)
    #Counter creates a dict
    #The Counter holds the data in an unordered collection,
    #just like hashtable objects. The elements here represent
    #the keys and the count as values.
    counts = Counter(list(counts.values()))[group_size]
    total+=counts
print(f"Solution 2:", total)