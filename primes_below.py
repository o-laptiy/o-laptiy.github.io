def is_prime(n):
	prime = True
	for i in range(2, 10):
		if (n % i == 0 and (n != i) or (n == 1)):
			prime = False
			break
	return(prime)
def primes_below(n):
	primes = []
	for i in range(1, n):
		t = is_prime(i)
		if (t == True):
			primes.append(i)
	print(primes)
primes_below(100)

