'''
Print all paths from left top corner to bottom right corner of a matrix. You can move right or down in each step. 

Example:
[['a', 'b', 'c'], 
['d', 'e', 'f']] 

Output: 
a->b->c->f 
a->b->e->f 
a->d->e->f
'''
    

a = [['a', 'b', 'c'], 
	 ['d', 'e', 'f']]

n = len(a)
m = len(a[0])


def nextStep(i=0,j=0,output=""):

	output+=str(a[i][j])
	if i+1 == n and j+1 == m:
		print(output)
	else:
		output+="->"
		if i+1 < n:
			nextStep(i+1,j,output)

		if j+1 < m:
			nextStep(i,j+1,output)

nextStep()