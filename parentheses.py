#Implement an algorithm to print all valid (e g , properly opened and closed) combinations of n-pairs of parentheses



N = 3

def printBrackets(n, opened=0, closed=0, output=""):
	if closed == n:
		print(output)
	else:
		if opened > closed:
			printBrackets(n, opened, closed+1, output+")")
		if opened < n:
			printBrackets(n ,opened+1, closed, output+"(")


printBrackets(N)