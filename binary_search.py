import random
import math 
import time

N = 10000
arr = [math.floor(random.random()*100) for _ in range(N)]
#print(arr)

element = arr[math.floor(random.random()*N)]
    
    
def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m

arr.sort()

print(element)

start_time = time.clock()
i = arr.index(element)
print("Built-in index\t--- %f seconds ---" % (time.clock() - start_time))
print(i)
print(arr[i])

start_time = time.clock()
i = binary_search(arr,element)
print("Binary search\t--- %f seconds ---" % (time.clock() - start_time))
print(i)
print(arr[i])
