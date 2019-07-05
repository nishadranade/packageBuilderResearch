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
    return distances
