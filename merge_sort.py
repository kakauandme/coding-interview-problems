import random
import math 
import time

N = 1000
arr = [math.floor(random.random()*100) for _ in range(N)]
#print(arr)

    
def merge_sort(a):
    
    if len(a)>1:
        l,r =  a[:len(a)//2], a[len(a)//2:]
        merge_sort(l)
        merge_sort(r)
        
        k=0
        j=0
        i=0
        while i < len(l) and j < len(r) :
            if l[i] < r[j]:
                a[k] = l[i]
                i+=1
            else:
                a[k] = r[j]
                j+=1
            k+=1
        
        if i < len(l):
            a[k:] = l[i:]
        else:           
            a[k:] = r[j:]


built_in = list(arr)
start_time = time.clock()
built_in.sort()
print("Built-in\t--- %f seconds ---" % (time.clock() - start_time))
#print(built_in)



merge = list(arr)
start_time = time.clock()
merge_sort(merge)
print("Merge\t--- %f seconds ---" % (time.clock() - start_time))
#print(merge)