import matplotlib.pyplot as plt
import numpy

E = 0.0001

def func(x):
    return 1 / x

def trapezoidFormula(interval, step):
    sum = 0
    for i in range(1, len(interval) - 1, 1):
        sum += func(interval[i])
    sum += (func(interval[0]) + func(interval[len(interval) - 1])) / 2
    return sum * step

def simpsonFormula(interval, step):
    sum = 0
    for i in range(1, len(interval) - 1, 1):
        if i % 2 == 1:
            sum += 4 * func(interval[i])
        else:
            sum += 2 * func(interval[i])
    sum += func(interval[0]) + func(interval[len(interval) - 1])
    return sum * (step / 3)

def doubleCalcTrap(start, end, step, interval):
    print("Trapezoid:")
    integrals = []
    for i in range(2):
        integrals.append(trapezoidFormula(interval, step))
        step /= 2
        interval = numpy.arange(start, end + step, step)
        print(integrals[i])

    i = 0
    while abs(integrals[i] - integrals[i + 1]) > E * 3:
        integrals.append(trapezoidFormula(interval, step))
        step /= 2
        interval = numpy.arange(start, end + step, step)
        print(integrals[i + 2])
        i += 1
    print("\n")

def doubleCalcSimp(start, end, step, interval):
    print("Simpson:")
    integrals = []
    for i in range(2):
        integrals.append(simpsonFormula(interval, step))
        step /= 2
        interval = numpy.arange(start, end + step, step)
        print(integrals[i])

    i = 0
    while abs(integrals[i] - integrals[i + 1]) > E * 3:
        integrals.append(simpsonFormula(interval, step))
        step /= 2
        interval = numpy.arange(start, end + step, step)
        print(integrals[i + 2])
        i += 1
    print("\n")

def graph(X, Y, descr, figureNum):
    plt.figure(figureNum)
    plt.plot(X, Y, label = descr)
    plt.legend()

start = 1.0
end = 2.0
n = 10
step = abs((end - start) / n)
interval = numpy.arange(start, end + step, step)

doubleCalcTrap(start, end, step, interval)
doubleCalcSimp(start, end, step, interval)

funcVal = []

for i in range(len(interval)):
    funcVal.append(func(interval[i]))
    
graph(interval, funcVal, "1/x", 1)
#graph(interval, Y, "intrp sin(2x)", 2)
plt.show()