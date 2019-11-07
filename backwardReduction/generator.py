import numpy as np
import random
import copy
import sys

# method to generate scenarios and their probabilities
def generateScenarios(n):
    scenarios = []
    for i in range(0, n):
        #scenarios.append(np.random.randint(3,12))
        scenarios.append(1/n)
    # total = sum(scenarios)
    # for i in range(0, n):
        # scenarios[i] = scenarios[i]/total
    return scenarios

def generateValues(n, mean1, std1, mean2, std2):
    # values = np.random.normal(mean, std_dev, n)
    # add uniform distribution support

    values1 = np.random.normal(mean1, std1, n)
    values2 = np.random.normal(mean2, std2, n)
    values = np.array([values1, values2])
    values = np.transpose(values)
    distances = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            distances[i][j] = np.linalg.norm(values[i] - values[j])
    return values, distances.tolist()

# master method
def generate(n, m1, std_1, m2, std_2):
    return generateScenarios(n), generateValues(n, m1, std_1, m2, std_2)


# method to generate the nxm matrix for super.py
def generateMatrix(n, m):
    #8 2
    means = np.random.normal(8, 2, n)
    std_devs = np.ones(n)
    values = np.random.normal(means, std_devs, (m, n))
    values = np.transpose(values)
    probs = np.ones(m)
    probs = probs * 1/m
    distances = np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            distances[i][j] = np.linalg.norm(values[:,i] - values[:, j])
    return values, distances, means, std_devs, probs



if __name__ == "__main__":
    random.seed(2)
    n = int(sys.argv[1])
    random.seed(5)
    a = generate(n)
    scenario_probabilies = a[0]
    distances = a[1]



# old method to generate the distances matrix ***OBSOLETE***
# def generateDistances(n):
#     distances = []
#     # initialize all distances to be -1
#     negOne = []
#     for i in range(0, n):
#         negOne.append(-1)
#     for i in range(0, n):
#         distances.append(copy.deepcopy(negOne))
#     # now randomly generate distances between 1 and 99, with all the values along the diagonal set to 100
#     for i in range(0, n):
#         for j in range(0, n):
#             if i == j:
#                 distances[i][j] = 0         # replace the 0 with a 100 if attempting to run runOld.py
#             if distances[i][j] == -1 and distances[j][i] == -1:
#                 distances[i][j] = 99*random.random()
#                 distances[j][i] = distances[i][j]
#     return distances
