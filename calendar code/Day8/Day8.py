op,num=[],[]
with open("/home/nico/Desktop/calendar code/Day8/list", "r") as fp:
    for el in fp:
        op.append(el.strip().split(' ')[0])#op= operation
        num.append(int(el.strip().split(' ')[1]))#num=number/value


def part1():
    cont=0
    acc=0
    l=[] #every time we find an element in a new position we add it to a list, if we add the same position to the list we return acc value before breaking the cycle 'cause we spotted a loop
    while cont<len(op):
        if (op[cont])=='jmp':
            if cont in l:
                print(acc)
                break
            
            l.append(cont)
            cont+=num[cont]#jmp is jumping to the value without adding accumulation     
            continue
        
        
        elif op[cont]=='nop':
            if cont in l:
                print(acc)
                break
            
            l.append(cont)
            cont+=1 #no operation is going down with the cycle without adding any value to accumulation
            continue 
        
        
        elif op[cont]=='acc':
            if cont in l:
                print(acc)
                break
            acc+=num[cont]# summing up on the accumulation parameter          
    
            l.append(cont)
            cont+=1
            continue

#part1()        

#indices funct is finding the indices of the position of either 'jmp' and 'nop'
def indi(op):        
    indices=[]
    for i in range(len(op)):
        if op[i]=='jmp' or op[i]=='nop':
            indices.append(i)
    return indices
indices=indi(op)


def swap(op, indices):
    blist=[]
    for i in indices:
        if op[i]=='jmp': #we invert one single the value, we put in the list the new 'op' operation list and we modify again the the initial value
            op[i]='nop'
            blist.append(list(op)) #it is important to use 'list' parameter cause lists are mutable elements!
            op[i]='jmp'         

        elif op[i]=='nop':
            op[i]='jmp'
            blist.append(list(op))
            op[i]='nop'


    return list(blist)

blist=swap(op,indices)

def part2(op): #it's similar to pt1 but with the main difference that returns 'value' only if there's no loop.
    cont=0
    acc=0
    l=[]
    while cont<int(len(op)+1):
        if cont== (int(len(op))):
            print('No loop, Values: ')
            print(acc)
            break
        if (op[cont])=='jmp':
            if cont in l:
                break
            
            l.append(cont)
            cont+=num[cont]    
            continue
        
        
        elif op[cont]=='nop':
            if cont in l:
                break
            
            l.append(cont)
            cont+=1
            continue 
        
        
        elif op[cont]=='acc':
            if cont in l:
                break
            acc+=num[cont]            
    
            l.append(cont)
            cont+=1
            continue
        

def main(blist):
    for el in blist:
        part2(el)
        
    
main(blist)




