for n in range(1,1001):
	if ((n % 3 == 0) & (n % 5 == 0)):
		print("FizzBuzz")
		continue
	elif (n % 3 == 0):
		print("Fizz")
	elif (n % 5 == 0):
		print("Buzz")
	else:
		print(n)