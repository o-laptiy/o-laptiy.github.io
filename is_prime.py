def is_prime(n):
	prime = True
	for i in range(2, 10):
		if (n % i == 0 and (n != i) or (n == 1)):
			prime = False
			break
	return(prime)
##for j in range(1, 21):
##        k = is_prime(j)
##        print("number %i is prime: %s" % (j, k))
