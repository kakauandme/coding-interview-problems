import random
import math 
import time

N = 1000
arr = [math.floor(random.random()*100) for _ in range(N)]
#print(arr)





def partition(a,s,e):
    p = a[e]
    i = s
    for j in range(s,e):
        if a[j] < p:
            a[i],a[j] = a[j],a[i]
            i+=1
    a[i], a[e] = a[e],a[i]
    return i
    
def q_sort(a,s=0,e=N-1):
    if s<e:
        pos=partition(a,s,e)
        q_sort(a,s,pos-1)
        q_sort(a,pos+1,e)


built_in = list(arr)
start_time = time.clock()
built_in.sort()
print("Built-in\t--- %f seconds ---" % (time.clock() - start_time))
#print(built_in)



quick_sort = list(arr)
start_time = time.clock()
q_sort(quick_sort)
print("Quick sort\t--- %f seconds ---" % (time.clock() - start_time))
#print(quicksort)
