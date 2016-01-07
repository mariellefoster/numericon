import math
from carmichael import *

#calculates if a number is "happy"
#ie if you repeatedly square each digit
#and add the squares, does it end in 1 or
#loop infinitely?
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

#binomial representation of a base 10 number
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

#brute force prime testing
def simple_prime_test(n):
    k = int(math.sqrt(n))+1
    n_1 = n
    factors = []
    for i in range(2, k):
        fact = 0
        while n%i == 0:
            n = n/i
            fact += 1
        if fact > 0:
            factors.append((i, fact))
        if n == 1:
            return factors
    if n > 1 and n != n_1:
        factors.append((n, 1))
    return factors

#string formats prime factors *so pretty*
def pretty_prime_factors(prime):
    val = ""
    for tup in prime:
        val += str(tup[0]) + "^" + str(tup[1]) + " * "

    return val[:len(val)-2]

def achilles(prime_fact):
    for i in prime_fact:
        if i[1] < 2:
            return False
    return True

#detects if n is a wilson prime, i.e. 
#if the factorial of n-1 plus 1 divided by n^2 is 0
def wilson(n):
    if (math.factorial(n-1) + 1) % (n*n) == 0:
        return True
    return False


#sigma function
def divisor_sum(primes, powers, current_div, current_res, factors):
    if current_div == len(primes):
        factors.append(current_res)
        return
    for i in range(0, powers[current_div]+1):
        divisor_sum(primes, powers, current_div+1, current_res, factors)
        current_res *= primes[current_div]
    


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

            #if PRIME
            prime_fact = simple_prime_test(n)
            if prime_fact == []:
                print n, "is a prime number"
                
        
                #wilson prime
                if wilson(n):
                    print "%i is a Wilson prime" % n

                #sophie germain
                if simple_prime_test(2*n+1) == []:
                    print "%i is a Sophie Germain prime" % n


                #emirp primes
            
            ###IF NOT PRIME###
            else:
                #prime factorization
                print "Prime Factorization:", pretty_prime_factors(prime_fact)

                #achilles number (all factors are squares or more)
                if achilles(prime_fact):
                    print "%i is an Achilles number." % n

                #carmichael
                if carmichael_test(n) == True:
                    print "%i is a Carmichael number" % n

                #split into primes and powers
                primes = [x[0] for x in prime_fact]
                powers = [x[1] for x in prime_fact]
                
                factors = []
                #sigma function
                divisor_sum(primes, powers, 0, 1, factors)

                #take off n itself at the end
                factors.sort()
                factors = factors[:-1]

                sum_factors = sum(factors)

                #perfect numbers
                if sum_factors == n:
                    print "%i is a perfect number" % n
                #abundant numbers
                elif sum_factors > n:
                    print "%i is an abundant number" % n
                #deficient numbers
                elif sum_factors < n:
                    print "%i is a deficient number" % n

            
                #amicable numbers
                # Let's take all the proper divisors of 220 (that is to say, 
                # all its divisors that leave no remainder, including the number 1, 
                # and excluding the number itself) and all them up:
                
                #find the divisors of the potential amicable number
                amicable_factorization = simple_prime_test(sum_factors)

                #split into primes and powers
                amicable_primes = [x[0] for x in amicable_factorization]
                amicable_powers = [x[1] for x in amicable_factorization]

                amicable_factors = []
                divisor_sum(amicable_primes, amicable_powers, 0, 1, amicable_factors)

                #take off n itself at the end
                amicable_factors.sort()
                amicable_factors = amicable_factors[:-1]

                #print pair if amicable
                sum_amicable = sum(amicable_factors)
                if sum_amicable == n:
                    print "%i and %i are an amicable number pair" % (n, sum_factors)
        

                #weird numbers

                #untouchable numbers

            
            ###OTHER###

                #reciprocal base ten fraction

                #representation as the sum of two squares

                #repunit, repdigit, and repunit primes

                #narcissistic numbers
            print

main()


