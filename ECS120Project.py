"""
This program is a nondeterministic solution to the factoring problem. The input is an integer M
as an ASCII string, and returns one of the nontrivial factors as another ASCII string.
"""
from threading import Thread
import utils
import math
import numpy

def ndFactor(inNum, K):
    num = int(inNum)
    numRt = int(math.sqrt(num))
    
    threads = []
    ndSoln = utils.NonDetSolution()
    
    numList = numpy.array_split(range(2, numRt + 1), K)
    for L in numList:
        t = Thread(target = findFactor, args = (L, num, ndSoln))
        threads.append(t)

    solution = utils.waitForOnePosOrAllNeg(threads, ndSoln)
    return solution
    
def findFactor(L, num, ndSoln):
    for i in L:
        if num % i == 0:
            ndSoln.setSolution(i)
          
def main():
    while True:
        number = float(input("Please a positive integer: "))
        if number > 0 and number % 1 == 0:
            break
        
    K = int(input("How many groups do you want to split the numbers into? ")) 
    print("One of the factors of the number you entered is:", ndFactor(number, K))

main()