#****** Software, Product, and Embedded Engineering Candidates ******

import math
# function to calculate next fibonacii
def nextFibonacci(a, b):
    return long(b), long(a+b)

# to check divisibility by 5,3
def checkDivisibility(a):
    retVal = ""
    if not a%5: retVal += "Fizz"
    if not a%3: retVal += "Buzz"
    return retVal

#t Check if a number is prime
def checkPrime(a):
    # if a is prime one of the factors should be < sqrt(a)
    sqrt = long(math.ceil(a ** (1 / 2.0)))
    for i in xrange(2,sqrt):
        if not a%i: return False
    return True

def main(num):
    # declaring first 2 numbers
    i_n_minus_1 = 0
    i_n = 1
    for i in range(2, num):
        i_n_minus_1, i_n = nextFibonacci(i_n_minus_1, i_n);
        retVal = checkDivisibility(i_n);
        if retVal == "":
            if checkPrime(i_n): retVal = "BuzzFizz"
            else: retVal = i_n
        print str(retVal) #print f(n)

if __name__ == '__main__':
        # input n to find f(n)
        try:
            num = int(input("Enter a number: "))
            main(num)
        except Exception, e:
            print "Some err " + str(e)
