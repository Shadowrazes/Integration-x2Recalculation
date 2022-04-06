import numpy

E = 0.0001

class InputData:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def func(x):
    return x / 10

def trapezoidFormula(interval, step):
    sum = 0
    for i in range(1, len(interval) - 1, 1):
        sum += func(interval[i])
    sum += (func(interval[0]) + func(interval[len(interval) - 1])) / 2
    return sum * step

def doubleCalc(start, end, step, interval):
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


data = [InputData(0, func(0)), InputData(1, func(1)), InputData(2, func(2)), InputData(3, func(3)), InputData(4, func(4))]
start = data[0].x
end = data[len(data) - 1].x
step = abs((end - start) / len(data)) / 2
interval = numpy.arange(start, end + step, step)

doubleCalc(start, end, step, interval)