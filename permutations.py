#Write a method to compute all permutations of a string



input = "abc"


def permutations(str, output=""):
	n = len(str)
	if n == 0:
		print(output)

	for i in range(n):
		permutations(str[:i] + str[i+1:], output+str[i])



permutations(input)