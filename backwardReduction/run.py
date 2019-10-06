from generator import *
from pMetricGeneral3 import *
from scatter import scatterPlot
from matplotlib import pyplot as plt
import sys
import time

# method to nicely print matrices
def printMatrix(matrix):
    for i in matrix:
        print(i)

# Super script to generate scenarios and distances and then do backward reduction on them
# Arguements are number of scenarios, and number of to be eliminated for eg python run.py 8 4  
if __name__=="__main__":
    start = time.time()
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    data = generate(n, 0, 1, 5, 2)
    # print("Scenarios:")
    #print(data[1][0])
    # print("Distances:")
    # printMatrix(data[1])
    # print()
    #scatterPlot(data[1][0])
    original = data[1][0]
    result = eliminateK(data[0], data[1][1], k, data[1][0])
    end = time.time()
    runTime = end - start
    print(str(n) + ", " + str(k) + ", " + str(runTime))
    #print("Reduced Scenarios:")
    #print(result[0])
    # print("Reduced Scenario Distances Matrix")
    # printMatrix(result[1])
    #scatterPlot(result[2])
    reduced = result[2]
    scatterPlot(original, reduced)