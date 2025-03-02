'''
This document mainly deals with some basic operations and the calculation of various commonly used values.
---Author: Season
---Language: Python
---Signature: S and A
              PHJsi
#############
#####---#####
###--   --###
#--S and A--#
###--   --###
#####---#####
#############
~~~~~~~~~~~~~
#############
#####---#####
###--   --###
#---PHJsi---#
###--   --###
#####---#####
#############
'''





from time import perf_counter
from sympy import solve


strCalc = lambda x:eval(x)

base2 = lambda x:eval('0b' + str(x))

base8 = lambda x:eval('0o' + str(x))

base16 = lambda x:eval('0x' + str(x))

base = lambda x, y: int(str(x), int(y))

toBase2 = lambda x:bin(x)

toBase8 = lambda x:oct(x)

toBase16 = lambda x:hex(x)

power = lambda x, y:x ** y
'''
def power(number:float,power:int) -> float:
    try:
        a = number ** power
        return a
    except:
        print("Input error: \"number\" should be in decimal form, \"power\" should be in ",\
            "integer form, but the passed in is not in decimal or integer form")
        exit()
'''

judgePower2 = lambda x:x & (x - 1)
'''
def judgePower2(number:int) -> bool:
    try:
        a = number & (number - 1) == 0
        return a
    except:
        print("Input error: \"number\" should be in integer form, but the passed in is not in integer form")
        exit()
'''

def judgePrime(number:int) ->bool:
    if number < 2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def FibonacciSequence(max:int) -> list:
    number,numA,numB = 0,0,1
    fib_list = []
    while number < max:
        fib_list.append(numB)
        numA,numB = numB,numA + numB
        number += 1
    return fib_list

def EQ(eq):
    ar=[]
    for i in eq.split():
        ar.append(i.replace("=","-(")+")")
    return solve(ar)




class ExtractRoot:
    def __init__(self,number:float,nbosr:int,epsilon:float = 0.0001) -> None:
        self.number = number
        self.NumberOfSquareRoot = nbosr
        self.epsilon = epsilon
        self.NumberOfOperations = 0
        self.low = 0.0
        self.high = self.number
        self.ans = (self.low + self.high) / 2.0

    def getNumberOfOperations(self) -> int:
        return self.NumberOfOperations

    def run(self) -> None:
        while abs(self.ans ** self.NumberOfSquareRoot - self.number) >= self.epsilon:
            self.NumberOfOperations += 1
            if self.ans ** self.NumberOfSquareRoot < self.number:
                self.low = self.ans
            else:
                self.high = self.ans
            self.ans = (self.high + self.low) / 2.0

    def getIntAns(self) -> int:
        return self.ans

class PI:
    def __init__(self,calculationTimes:int = 100) -> None:
        self.pi = 0
        self.N = calculationTimes
        self.start = perf_counter()
        for k in range(self.N):
            self.pi += 1 / pow(16,k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
        self.time = perf_counter() - self.start

    def __str__(self) -> str:
        return "The value of PI is:{}".format(self.pi) + ",Run time is:{:.5f}s".format(self.time)

    def get_IntPi(self) -> int:
        return self.pi

    def get_IntTime(self) -> int:
        return self.time

class SolutionOfHanoiTowerProblem3:
    ProblemSolution = []

    
    def __init__(self,number:int,a:str,b:str,c:str) -> None:
        if (number == 1):
            self.ProblemSolution.append([a,c])
            return
        self.__init__(number - 1,a,c,b)
        self.__init__(1,a,b,c)
        self.__init__(number - 1,b,a,c)
    
    def get_ProblemSolution(self) -> list:
        return self.ProblemSolution

class Circle:
    def __init__(self,radius:float,PI:float = 3.14) -> None:
        self.r = radius
        self.pi = PI
    
    def get_Perimeter(self) -> float:
        return self.r * 2 * self.pi
    
    def get_TheMeasureOfArea(self) -> float:
        return self.r ** 2 * self.pi





if __name__ == "__main__":
    print("Welcome to my library: calculation.py!")
