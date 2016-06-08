import random
import math 
import time

N = 1000
arr = [math.floor(random.random()*100) for _ in range(N)]
#print(arr)

def bubble_sort(a):
    notSorted = True
    while notSorted:
        notSorted = False
        for i in range(len(a)-1):
            if(a[i] > a[i+1]):
                a[i+1], a[i] = a[i],a[i+1]
                notSorted=True


built_in = list(arr)
start_time = time.clock()
built_in.sort()
print("Built-in\t--- %f seconds ---" % (time.clock() - start_time))
#print(built_in)

bubble = list(arr)
start_time = time.clock()
bubble_sort(bubble)
print("Bubble\t--- %f seconds ---" % (time.clock() - start_time))
#print(bubble)