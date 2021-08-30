#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:29:37 2021

@author: nico
"""
import re
f=open('list')
s=''
for el in f:
    s+=el
lista=s.split('\n\n')
li=[]
for el in lista:
    li.append(el.split())

s=0
filt1=[] #if cid variable is missing is still good
for el in li:
    if (len (el))==8:
        filt1.append(el)
    if (len (el))==7:
        b=''
        for i in el:
            b+=(i[:3])
        if 'cid' not in b:
            filt1.append(el)
                
#create a dict with type ':' and values per person
passports=[]
for person in filt1:
        passports.append(dict(x.split(':') for x in person)) #amazing
        
        
valid_passports=[]
values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for person in passports:
        if (1920 <= int(person['byr']) <= 2002
                and (2010 <= int(person['iyr']) <= 2020)
                and (2020 <= int(person['eyr']) <= 2030)
                and
                ((person['hgt'][-2:] == 'cm' and 150 <= int(person['hgt'][:-2]) <= 193)
                  or (person['hgt'][-2:] == 'in' and 59 <= int(person['hgt'][:-2]) <= 76))
                and (re.match(r'#[\da-f]{6}', person['hcl']))
                and (person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                and (re.match(r'\d{9}', person['pid']))):
                    valid_passports.append(person)
            
print(len(valid_passports)-1)



    





