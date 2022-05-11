def is_prime(n):
	prime = True
	for i in range(2, 10):
		if (n % i == 0 and (n != i) or (n == 1)):
			prime = False
			break
	return(prime)
primes = []
for i in range(10000, 100000):
	t = is_prime(i)
	if (t == True):
		primes.append(i)
pal_primes = []
for number in primes:
	listnum = list(map(int, str(number))) ## convert the number to the list
	listnum_reversed = list(reversed(listnum)) ## reverse the list with the number
	if listnum == listnum_reversed: ## check if reverse is equal to the initial number
		pal_primes.append(number)
print(pal_primes)
