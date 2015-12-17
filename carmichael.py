#a program to calculate carmichael numbers
#takes a while, looking into faster algorithms
import math

def carmichael_test(i):
	n = 2
	while n < i:
		if (n**i % i) != n:
			return False
		n += 1
	return True

def composite(i):
	n = 2
	while n < (math.sqrt(i)+1):
		if i%n == 0:
			return True
		n += 1
	return False