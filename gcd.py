#generates two 100 digit numbers and finds their gcd

from random import randint

def gcd(a, b):
	if b == 0:
		return
	steps +=1
	q = a/b
	r = a - b*q
	print "r: " + str(r)
	if (r > b):
		gcd(r, b)
	else:
		gcd(b, r)


