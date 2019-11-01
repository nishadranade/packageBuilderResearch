import numpy as np
import cplex
import scipy.stats import norm
import sys

def generateData(n, m):
    # generate m samples each for n normal distributions
    # return grid of size n x m
    return data


def solve_cplex(v, p, n, m):
    data = generateData(n, m)
    d = np.asarray(data)
    T_i = np.sum(d, axis = 1)

    problem = cplex.Cplex()

    problems.variables.add(types = [problem.variables.type.binary]*n)

# add objective of the cplex problem
    pairs = zip(range(0,n), T_i.tolist())
    problem.objective.set_sense(problem.objective.sense.minimize)
    problem.objective.set_linear(pairs)

    
