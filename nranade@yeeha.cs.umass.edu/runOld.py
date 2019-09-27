from generator import *
from pMetricGeneralOld import *
import sys

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
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    data = generate(n)
    print("Scenarios:")
    print(data[0])
    print("Distances:")
    printMatrix(data[1])
    print()
    result = deleteK(data[0], data[1], k)
    print("Reduced Scenarios:")
    print(result[0])
    print("Reduced Scenario Distances Matrix")
    printMatrix(result[1])