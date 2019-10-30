import numpy as np
import random
import cplex 
import scipy as sp
from scipy.stats import norm
import sys

def extract_data(file_name):
    with open(file_name) as f:
        file = f.read()
    
    file = file.split('\n')

    mean = [row.split(', ')[0] for row in file]
    std_dev = [row.split(', ')[1] for row in file]

    return (mean, std_dev)

def solve_cplex(mean, std_deviation, v, p):
    # random.seed(100)

    # t = np.random.normal(0, 1, 3)
    # p = 0.9

    # pass in a list of variables each with provided means and standard deviations, as well as v and p

    # let us for simplicity assume that all t_i are std normal
    # all x_i are binary

    # let t_1 = (1, 1), t_2 = (2, 1), t_3 = (3, 1)
    # v = 5

    problem = cplex.Cplex()

    #Data Declaration
    ti_mu = mean
    ti_sigma = std_deviation

    num_decision_var = len(ti_mu)

    #names = ["x_1", "x_2", "x_3", "c"]
    names = [str(i) for i in range(num_decision_var+1)]
    #names.append('c')

    problem.variables.add(names=names)

    # problem.variables.set_types( [
    #     ("x_1", problem.variables.type.binary),
    #     ("x_2", problem.variables.type.binary),
    #     ("x_3", problem.variables.type.binary),
    #     ("c", problem.variables.type.continuous)        
    # ])

    for i in range(len(names)-1):
        problem.variables.set_types(i, problem.variables.type.binary)
    problem.variables.set_types(len(names)-1, problem.variables.type.continuous)

    #Objective
    problem.objective.set_sense(problem.objective.sense.minimize)
    objective = ti_mu#[ 1, 2, 3, 0]
    objective.append(0)
    pairs = zip(names, objective)
    problem.objective.set_linear(pairs)

    #Linear Constraint
    #p = 0.9
    phi_p = norm.ppf(p)
    lin_val = ti_mu
    lin_val.append(-phi_p)
    # print(t)
    #lin_constraint = [["x_1", "x_2", "x_3", "c" ], [1, 2, 3, -phi_p]]
    lin_constraint = [names, lin_val]
    #v = -1
    problem.linear_constraints.add(lin_expr=[lin_constraint], rhs=[v], senses='G')


    #constraint_senses = ["G"]
    #Quadratic Constraint
    #quad_constraint = cplex.SparseTriple(ind1 = ["x_1", "x_2", "x_3", "c" ], ind2= ["x_1", "x_2", "x_3", "c" ], val = [1,1,1,-1])  
    quad_val = ti_sigma
    quad_val.append(-1)
    quad_constraint = cplex.SparseTriple(ind1 = names, ind2= names, val = quad_val)  
         
    problem.quadratic_constraints.add(rhs = 0.0, quad_expr=quad_constraint, name="Q", sense='L')

    #Solve
    problem.solve()
    print(problem.solution.get_values())
    print(problem.solution.get_objective_value())

if __name__=='__main__':
    file_name = sys.argv[1]     #CSV file name
    v = sys.argv[2]             #v
    p = sys.argv[3]             #p

    data = extract_data(file_name)
    mean = data[0]
    std_deviation = data[1]

    solve_cplex(mean, std_deviation, v, p)

