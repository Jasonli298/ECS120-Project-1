"""
This program is a nondeterministic solution to the factoring problem. The input is an integer M
as an ASCII string, and returns one of the nontrivial factors as another ASCII string.
"""
from threading import Thread
import utils
import math
import numpy

def ndFactor(inString, K):
    num = int(inString)
    numRt = int(math.sqrt(num))
    
    threads = []
    ndSoln = utils.NonDetSolution()
    
    numList = numpy.array_split(range(2, numRt), K)
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
    number = input("Enter a positive integer: ")
    print("One of the factors of the number you entered is:", ndFactor(number, 10))

main()