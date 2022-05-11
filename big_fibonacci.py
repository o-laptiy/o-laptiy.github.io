def big_fibonacci(n):
	n0 = 1
	n1 = 1
	t = 1
	while (len(str(n1)) != n):
		t = n0 + n1
		n0 = n1
		n1 = t
	print(t)
big_fibonacci(1)
big_fibonacci(2)
big_fibonacci(3)
big_fibonacci(5)
big_fibonacci(30)