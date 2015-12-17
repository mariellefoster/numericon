#a program to calculate carmichael numbers
#takes a while, looking into faster algorithms
import math

def carmichael_test(i):
	n = 2
	while n < i:
		if modular_exponentiation(n, i, i) != n:
			return False
		n += 1
	return True


# n**e % m
def modular_exponentiation(n, e, m):
	x = 1
	while e > 0:
		if e %2 == 0:
			n = (n * n) % m
			e = e/2
		else:
			x = (n * x) % m
			e = e - 1
	return x 