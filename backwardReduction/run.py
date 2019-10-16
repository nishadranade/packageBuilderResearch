from generator import *
from pMetricGeneral3 import *
from scatter import *
from matplotlib import pyplot as plt
import copy
import sys
import time

# method to nicely print matrices
def printMatrix(matrix):
    for i in matrix:
        print(i)

def savePlot(data, n, k):
    data_1 = data
    temp = copy.deepcopy(data_1)

    ratio = k / n
    interval = int((ratio / 3)*n)

    min_p = 0
    max_p = 0
    eliminated_results = []
    for i in range(0, k+1, interval):
        result = eliminateK(data_1[0], data_1[1][1], i, data_1[1][0])    #fix
        reduced_values = copy.deepcopy(result[2])           #result[2]
        reduced_probabilities = copy.deepcopy(result[0])    #result[0]
        eliminated_results.append((reduced_values, reduced_probabilities, i))
        min_p = min(min_p, min(reduced_probabilities))
        max_p = max(max_p, max(reduced_probabilities))
        #singleScatterPlot(reduced_values, reduced_probabilities, n, i)
        data_1 = copy.deepcopy(temp)
    
    for scenario in eliminated_results:
        singleScatterPlot(scenario[0], scenario[1], n, scenario[2], min_p, max_p)


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
    original = data[1][0]
    original_probabilities = copy.deepcopy(data[0])
    result = eliminateK(data[0], data[1][1], k, data[1][0])
    end = time.time()
    runTime = end - start
    print(str(n) + ", " + str(k) + ", " + str(runTime))
    #print("Reduced Scenarios:")
    #print(result[0])
    # print("Reduced Scenario Distances Matrix")
    # printMatrix(result[1])

    data_1 = generate(n, 0, 1, 5, 2)
    savePlot(data_1, n, k)

    reduced = result[2]
    reduced_probabilities = result[0]
    #scatterPlot(original, original_probabilities, reduced, reduced_probabilities)
    #singleScatterPlot(reduced, reduced_probabilities, n, k)
    