import math

def main():
	for i in range(30, 30000):
		if not (composite(i)):
			if not (composite(i-28)):
				if not (composite(i+28)):
					print i-28, i, i+28


def composite(i):
	n = 2
	while n < (math.sqrt(i)+1):
		if i%n == 0:
			return True
		n += 1
	return False



main()