import numpy as np
import random
import copy

# method to generate scenarios and their probabilities
def generateScenarios(n):
    scenarios = []
    for i in range(0, n):
        scenarios.append(np.random.randint(3,12))
    total = sum(scenarios)
    for i in range(0, n):
        scenarios[i] = scenarios[i]/total
    return scenarios

# method to generate the distances matrix
def generateDistances(n):
    distances = []
    # initialize all distances to be -1
    negOne = []
    for i in range(0, n):
        negOne.append(-1)
    for i in range(0, n):
        distances.append(copy.deepcopy(negOne))
    # now randomly generate distances between 1 and 99, with all the values along the diagonal set to 100
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                distances[i][j] = 100
            if distances[i][j] == -1 and distances[j][i] == -1:
                distances[i][j] = 99*random.random()
                distances[j][i] = distances[i][j]
    return distances

# master method
def generate(n):
    return generateScenarios(n), generateDistances(n)

print(generate(5))