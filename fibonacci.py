#Write a method to generate the nth Fibonacci number

import time


N = 30
def fibonacci(n):
	if n > 1:
		return fibonacci(n-2) + fibonacci(n-1)
	else:
		return n




def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return b

f = 0
start_time = time.clock()
f= fibonacci(N)
print("Recursive\t--- %f seconds ---" % (time.clock() - start_time))
print(f)

start_time = time.clock()
f= fib(N)
print("Loop\t--- %f seconds ---" % (time.clock() - start_time))
print(f)