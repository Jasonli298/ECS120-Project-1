# ECS120 Project1

I attempetd to write a nondeterministic python program that
solves the factoring problem. I referenced the `containsNANA()` function in the book, and modified the program a little to suit the task more.

First, I calculated the square root of the number `num` entered, since I only need to check the numbers ranging from 2 to $sqrt{num}$, and the rest of the factors can be easily obtained by dividing `num` by the factors found. 

Then I used the `array_split()` function in the imported `numpy` module to split `num` into *K* groups.
```python
for L in numList:
    t = Thread(target = findFactor, args = (L, num, ndSoln))
    threads.append(t)
```
This block creates a thread for each of the *K* groups, and appends it to the `threads` list. Then I used the `waitForOnePosOrAllNeg()` function in the `utils` module to start the threads. Then I return the `solution` that contains one of the factors of `num` as a string.

The `findFactor()` function first iterates through one of the arrrays we obtained by `array_split()`
```python
for i in L:
    if num % i == 0: #determines if i divides num
        ndSoln.setSolution(i)
```
The resulting program correctly behaves, however it only obtains one of the factors of `num`. Since I'm not entirely sure about the behavior of the `setSolution()` or `getSolution()` functions in the `NonDetSolution` class, I will try to write another version of `findFactor()` here.

```python
def findFactor(L, num, ndSoln):
    currentSolution = ndSoln.getSolution()
    for i in L:
        if num % i == 0:
            if currentSolution == "no":
                ndSoln.setSolution(i)
            else:
                newSolution = currentSolution + " " + str(i)
                ndSoln.setSolution(newSolution)
```
