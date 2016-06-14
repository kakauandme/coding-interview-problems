#Given an in nite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.




coins = (1,5,10,25)


def getChange(amount, output=""):

	suitable = [c for c in coins if c <= amount]
	
	
	n = len(suitable)
	if n ==0:
		print(output)
	else:
		#all suitable 
		#for coin in suitable:			
		#	getChange(amount-coin, output+str(coin)+" ")
		#optimal
		coin = suitable[-1]
		getChange(amount-coin, output+str(coin)+" ")

getChange(6)