import math
from carmichael import *

def is_happy(n):
    h = set()
    n = str(n)

    while n != "1":
        if n in h:
            return False
        total = 0
        for i in n:
            total += int(i)*int(i)
        h.add(n)
        n = str(total)
    return True


def bin_rep(n):
    i = -1
    n1 = n
    while n1 > 0:
        i += 1
        n1 = n1/2
    bin = ""
    for j in range(i, -1, -1):
        jpow = pow(2, j)
        if jpow <= n:
            bin += "1"
            n = n % jpow
        else:
            bin += "0"
    return bin




def main():

    inpt = None
    print "Welcome to Numericon! \nPlease enter in a integer you wish to know more about. \nType q to exit. \n"

    while inpt != "q":
        inpt = raw_input("Enter your integer here: ")

        while not inpt.isdigit() and inpt != "q":
            inpt = raw_input("Enter a real integer here (you goofed on your last one): ")

        if inpt != "q": 
            n = int(inpt)
            print "~~~~~~~~~~"
        
            ###BASIC###

            #happy number
            if is_happy(n):
                print "%i is Happy" % n

            #binary representation
            print "Binary representation of %s: %s" % (n, bin_rep(n))


        ###PRIME###
        
            #wilson prime

            #sophie germain

            #prime

            #emirp primes
        
        ###IF NOT PRIME###

            #prime factorization

            #achilles number (all factors are squares or more)

            #carmichael
            if carmichael_test(n) == True:
                print "%i is a Carmichael number" % n

            #amicable numbers
            # Let's take all the proper divisors of 220 (that is to say, 
            # all its divisors that leave no remainder, including the number 1, 
            # and excluding the number itself) and all them up:

            #abundant numbers

            #weird numbers

            #untouchable numbers

            #perfect numbers


        ###OTHER###

            #reciprocal base ten fraction

            #representation as the sum of two squares

            #repunit, repdigit, and repunit primes

            #narcissistic numbers

        #

main()


