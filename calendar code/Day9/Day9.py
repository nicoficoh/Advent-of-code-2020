l=[]
with open("/home/nico/Desktop/calendar code/Day9/list", "r") as fp:
    for el in fp:
        l.append(int(el.strip()))

n=25 #this parameter change according to the dimension of probe
cont=n+1
#grouping returns a dict of every number after the probe a list of
#the previous elements after that number
def grouping():
    
    groups={}
    global cont
    
    for el in range(len(l)):      
        for i in range(cont-n-1, cont-1):
            num= l[el+n]
            if not num in groups:
                groups[num]=[l[i]]
            else:
                groups[num].append(l[i])
        if cont==len(l):
            break
        cont+=1
    return (groups)

groups= grouping()


import itertools
#itertools it is helping us with combinations

def issum():
    k2=[]
    for k,v  in groups.items():
        comb=list(itertools.combinations(v, 2))#pair combination inside each group of elements
        for el in comb:
            s=0
            for i in el:
                s+=i
            if s== k:#when the sum of the combination is eual to the number we add the value to a list
                k2.append(k)
    inter=set(groups.keys()) ^ set(k2) #we exclude all the elements that are not equal among the two lists
    return inter.pop()#this is our result
  
value= issum() #the result of part1 it is used in part2

#PART TWO IS DIFFERENT
#we are looking for the consecutive elements that summed up are the result of part1
def karinacolo():
    s=0
    pos=0
    
    while pos < (len(l)):
        lista=[]
        for i in range(pos, len(l)):
            s+=l[i] 
            lista.append(l[i]) #we append element to the list, in this case we know the element that met the criteria
            if s==value :
                return (min(lista)+max(lista)) #sol pt2 are the sum of the min and max of this list
            
            elif s>value: #if the the sum exceed the expected value we initialize again the summatory before breaking the cycle and 
                s=0
                lista=0
                break
        pos+=1 #we add a position
sol2= karinacolo()
print(sol2)
