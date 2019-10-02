from generator import *
#from pMetricGeneral import *
from pMetricGeneral3 import *
import sys
import time

# method to nicely print matrices
def printMatrix(matrix):
    for i in matrix:
        print(i)

# # method to put result matrices into a file
# def saveResults(matrix):
#     with open('results.txt', 'w') as f:
#         f.write("Reduced Scenarios: \n[")
#         for i in matrix[0]:
#             f.write("%s," %i)
#         f.write("]\n")

# Super script to generate scenarios and distances and then do backward reduction on them
# Arguements are number of scenarios, and number of to be eliminated for eg python run.py 8 4  
if __name__=="__main__":
    start = time.time()
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    data = generate(n, 0, 1, 5, 2)
    # print("Scenarios:")
    # print(data[0])
    # print("Distances:")
    # printMatrix(data[1])
    # print()
    result = eliminateK(data[0], data[1], k)
    end = time.time()
    runTime = end - start
    print(str(n) + ", " + str(k) + ", " + str(runTime))
    # print("Reduced Scenarios:")
    # print(result[0])
    # print("Reduced Scenario Distances Matrix")
    # printMatrix(result[1])
