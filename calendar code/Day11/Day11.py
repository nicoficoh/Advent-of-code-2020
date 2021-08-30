#!/usr/bin/env pxthon3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:26:39 2021

@author: nico
"""

plane = [line.strip() for line in open("/home/nico/Desktop/calendar code/Day11/list", "r")]

def square(y,x,plane): #y e x della nostra cella
    nove=[]
    s=0
    cella=plane[y][x]
    su= plane[y-1][x]
    susi=plane[y-1][x-1]
    si=plane[y][x-1]
    
    if x<(len(plane[0])-1): #avoid indey out of range
        sude=plane[y-1][x+1]
        de=plane[y][x+1]
        
    if y< (len(plane)-1):
        gisi=plane[y+1][x-1]
        gi=plane[y+1][x]
        
    if y< (len(plane)-1):
        if x<(len(plane[0])-1):
            gide=plane[y+1][x+1]
            
        

    
    if y==0: #se ci troviamo sul bordo superiore
        if x==0:
            nove.append((cella,de,gi,gide))
        elif x==(len(plane[0])-1):
            nove.append((si,cella,gisi,gi))
        else:
            nove.append((si,cella,de,gisi,gi,gide))
           
            
    elif x==0: #se ci troviamo sul bordo a sinistra
        if y==0: #l'abbiamo gia fatta, e non dobbiamo ripeterla
            s+=1
        elif y==(len(plane)-1):
            nove.append((su,sude,cella,de))
        else:
            nove.append((su,sude,cella,de,gi,gide))
            
    elif y==(len(plane)-1):
        if x==0:
            s+=1
        elif x==(len(plane[0])-1):
            nove.append((susi,su,si,cella))
        else:
            nove.append((susi,su,sude,si,cella,de))
    elif x==(len(plane[0])-1):
        if y==0:
            s+=1
        elif y==(len(plane)-1):
            s+=1
        else:
            nove.append((susi,su,si,cella,gisi,gi))
    else:
        nove.append((susi,su,sude,si,cella,de,gisi,gi,gide))
    return( nove)

def modify(t,y,x,plane): #modifyfica l'aereo utiliyyando le coordinate

    riga=(plane[y])
    nriga = riga[:x] +t + riga[x + 1:]
    plane[y]=nriga

        
    return (plane)
    

def coordinate(): #ritorna le coordinatete di ogni singola cella
    coordinatetes=[]
    y,x=0,0
    for riga in plane:
        
        for posto in riga:
            coordinatetes.append((posto,y,x))
            x+=1
        y+=1
        x=0
    return coordinatetes



def occupy(coordinatetes): #se trova vuoto occupy,ritorna le coordinatete
    new=[]
    for coor in coordinatetes:
        cubo=square(coor[1],coor[2],plane)
        if coor[0]=='L':
            for el in cubo:
                
                if '#' not in el:
                    new.append(('#',coor[1],coor[2]))  #if it is a dot it won't be inside
                else:
                    new.append(('L',coor[1],coor[2]))
        if coor[0]=='#':
            new.append(('#',coor[1],coor[2]))

    return(new)


def newplane(coor):  #modifyfica irrimediabilmente l'aereo
    for el in coor:
        modify(el[0],el[1],el[2],plane)
    return plane



def free(coordinatetes):
    new=[]
    for coor in coordinatetes:
        cubo=square(coor[1],coor[2],plane)
        if coor[0]=='#':
            for el in cubo:
                if (el.count('#'))>4:
                    new.append(('L',coor[1],coor[2]))
                else:
                    new.append(('#',coor[1],coor[2]))
        if coor[0]=='L':
            new.append(('L',coor[1],coor[2]))
            
    return new

# this is the loop necessary
def block():
    coordinatetes=coordinate()
    occupyte=occupy(coordinatetes)
    newplane(occupyte)    
    coordinatetes2=coordinate()    
    libecoor=free(coordinatetes2)
    newplane(libecoor)
    

def main():    
    for i in range(100):
        s=0
        block()        
        for riga in plane:
            s+=(riga.count('#'))
        print(s)


#Part2
#Instead of adiacent seats, we consider the first visible seat in each direction
           
                
            
            
def visible(x,y):
    s=0
    #print('E')
    for i in range(x+1, (len(plane[0]))): #range ultimo numero sempre escluso        
        if (plane[y][i])=='#':
            s+=1
            break
        if (plane[y][i])=='L':
            break   

        
        
    # print('O')
    for i in range(x-1,-1,-1):
    
        if (plane[y][i])=='#':
            s+=1
            break
        if (plane[y][i])=='L':
            break

            
                    
    # print('S')
    for i in range(y+1, len(plane)):
        if (plane[i][x])=='#':
            s+=1
            break
        if (plane[i][x])=='L':
            break

        
    # print('N')
    for i in range(y-1,-1,-1):
        if (plane[i][x])=='#':
            s+=1
            break
        if (plane[i][x])=='L':
            break

        
    #print('NE')
    limy=y
    limx=len(plane[0])-x -1
    for i in range(1,min(limy,limx)+1):

        if plane[y-i][x+i]=='#':
            s+=1
            break
        if plane[y-i][x+i]=='L':
            break


    # # print('N0')
    limy=y
    limx=x
    for i in range(1,min(limy,limx)+1):
        # print(x-i,y-i)
        if (plane[y-i][x-i])=='#':
            s+=1
            break
        if (plane[y-i][x-i])=='L':
            break


    # print('S0')
    limy=len(plane)-y
    limx=x+1
    for i in range(1,min(limy,limx)):
        if plane[y+i][x-i]=='#':
            s+=1
            break
        if plane[y+i][x-i]=='L':
            break


    # print('SE')
    limy=len(plane)-y
    limx=len(plane[0])-x
    for i in range(1,min(limy,limx)):
        if plane[y+i][x+i]=='#':
            s+=1
            break
        if plane[y+i][x+i]=='L':
            break
    
    return(s)


def freemi(coordinatetes):
    new=[]
    for coor in coordinatetes:
        if coor[0]=='#':
            s=visible(coor[2],coor[1])
            if s>4:
                new.append(('L',coor[1],coor[2]))
            else:
                new.append(('#',coor[1],coor[2]))
        else:
            continue
    return new

def occupyme(coordinatetes):
    new=[]
    for coor in coordinatetes:
        if coor[0]=='L':
            s=visible(coor[2],coor[1])
            if s==0:
                new.append(('#',coor[1],coor[2]))
            else:
                new.append(('L',coor[1],coor[2]))
        else:
            continue
    return new
                
        
def block2():
    coordinatetes=coordinate()
    occupyte=occupyme(coordinatetes)
    newplane(occupyte)    
    coordinatetes2=coordinate()    
    libecoor=freemi(coordinatetes2)
    newplane(libecoor)

def main2():    
    for i in range(100):
        s=0
        block2()        
        for riga in plane:
            s+=(riga.count('#'))
        print(s)

main2()