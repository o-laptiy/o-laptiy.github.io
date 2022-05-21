def is_prime(n):
	prime = True
	i = 2
	while(i * i <= n and prime != False):
		if (n % i == 0):
			prime = False
		i += 1
	return(prime)
##for j in range(1, 175):
##        k = is_prime(j)
##        if (k == True):
##        	print("number %i is prime" % (j))
