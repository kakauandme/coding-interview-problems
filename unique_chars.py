#Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?



false_input = "Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?";
true_input = "qwerty";


def unique_chars(s):
	n = len(s)
	
	for i in range(n):
		for j in range(i+1,n):
			#print("%d,%d"%(i,j))
			if s[i] == s[j]:
				return False
	return True

print(unique_chars(false_input))
print(unique_chars(true_input))