#Write code to reverse a C-Style String (C-String means that “abcd” is represented as  ve characters, including the null character )


input = list("Write code to reverse a C-Style String (C-String means that “abcd” is represented as  ve characters, including the null character )");
input.append(None);

n = len(input)
for i in range((n-1)//2):
	input[i], input[n-2-i] = input[n-2-i], input[i]

#print(input)
print("".join(input[:-1]))