import numpy as np
import cplex
import scipy.stats import norm
import sys

# ** make super class that will generate, reduce, pass the reduced stuff
# to cplex

# change the function to take nxm array as input, which is assumed to be
# reduced scenarios. Each of the m scenarios will also have a probability
# associated with them, which will be passed in as a vector of probabilities
# pass in the "actual" means

def generateData(n, m):
    # generate m samples each for n normal distributions
    # return grid of size n x m
    return data


def solve_cplex(v, p, n, data, probs, means):
    # data = generateData(n, m)
    d = np.asarray(data)
    # T_i = np.sum(d, axis = 1)

    m = data.shape[1]
    assert m == len(probs)

    problem = cplex.Cplex()

    problem.variables.add(types = [problem.variables.type.binary]*n)

# Warning- the following operations assume that the value of m is updated
# when the number of scenarios is reduced

# add M y_js which are indicator constraints (type binary)
    problem.variables.add(types = [problem.variables.type.binary]*m)

# add the indicator constraints on y_js
    for j in range(0, m):
        problem.indicator_constraints.add(
            indvar=n+j, complemented=0, rhs=v, sense="G",
            lin_expr=cplex.SparsePair(ind=list(range(0,n))), val=data[:,j].tolist())

# add last constraint that avg of y_j GE p
    problem.linear_constraints.add(lin_expr=[range(n,n+m), probs],
        senses=["G"], rhs=[p])

# add objective of the cplex problem
    pairs = zip(range(0,n), means)
    problem.objective.set_sense(problem.objective.sense.minimize)
    problem.objective.set_linear(pairs)

    problem.solve()

    return problem.solution.get_values(), problem.solution.get_objective_value()
