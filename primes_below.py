def is_prime(n):
	prime = True
	i = 2
	if(n == 1):
		prime = False
	while(i * i <= n and prime != False):
		if (n % i == 0):
			prime = False
		i += 1
	return(prime)
def primes_below(n):
	primes = []
	for i in range(1, n):
		t = is_prime(i)
		if (t == True):
			primes.append(i)
	print(primes)
primes_below(100)

