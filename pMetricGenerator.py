import numpy as np

# method to generate distances matrix

def generateScenarios(n):
    scenarios = []
    for i in range(0, n):
        scenarios.append(np.random.randint(3,12))
    total = sum(scenarios)
    for i in range(0, n):
        scenarios[i] = scenarios[i]/total
    return scenarios

def generateDistances(n):
    distances = []
    # initialize all distances to be -1
    negOne = []
    for i in range(0, n):
        negOne.append(-1)
    for i in range(0, n):
        distances.append(negOne)
    # now randomly generate distances between 1 and 99, with all the values along the diagonal set to 100
    return distances

print(generateDistances(5))
    
