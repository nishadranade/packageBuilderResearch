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

    problem = cplex.Cplex()

    #Data Declaration
    ti_mu = mean
    ti_sigma = std_deviation

    num_decision_var = len(ti_mu)

    decision_variables = range(num_decision_var)
    c = num_decision_var

    #names = ["x_1", "x_2", "x_3", "c"]
    # names = [int(i) for i in range(num_decision_var+1)]     #num_decision_var+1 is for the 'c' continuous decision variable

    # problem.variables.add(names=names)
    problem.variables.add(types= [problem.variables.type.binary]*num_decision_var)
    problem.variables.add(types= [problem.variables.type.continuous])

    # for i in range(len(names)-1):
    #     problem.variables.set_types(i, problem.variables.type.binary)
    # problem.variables.set_types(len(names)-1, problem.variables.type.continuous)

    #Objective
    problem.objective.set_sense(problem.objective.sense.minimize)
    objective = ti_mu  #[ 1, 2, 3, 0]
    #objective.append(0)
    pairs = zip(decision_variables, objective)
    problem.objective.set_linear(pairs)

    #Linear Constraint
    phi_p = norm.ppf(p)
    lin_val = ti_mu
    lin_val.append(-phi_p)
    # print(t)
    #lin_constraint = [["x_1", "x_2", "x_3", "c" ], [1, 2, 3, -phi_p]]
    lin_constraint = [decision_variables, lin_val]
    #v = -1
    problem.linear_constraints.add(lin_expr=[lin_constraint], rhs=[v], senses='G')


    # linear constraint to limit the number of 1s in the objective
    cons = np.ones(num_decision_var).tolist()
    lin_constraint2 = [decision_variables, cons]
    problem.linear_constraints.add(lin_expr=[lin_constraint2], rhs=[10], senses='L' )

    #Quadratic Constraint
    #quad_constraint = cplex.SparseTriple(ind1 = ["x_1", "x_2", "x_3", "c" ], ind2= ["x_1", "x_2", "x_3", "c" ], val = [1,1,1,-1])  
    quad_val = ti_sigma
    quad_val.append(-1)
    quad_constraint = cplex.SparseTriple(ind1 = list(decision_variables)+[c], ind2= list(decision_variables)+[c], val = quad_val)  
         
    problem.quadratic_constraints.add(rhs = 0.0, quad_expr=quad_constraint, name="Q", sense='L')

    #Solve
    problem.solve()
    print(problem.solution.get_values())
    print(problem.solution.get_objective_value())

if __name__=='__main__':
    #file_name = sys.argv[1]     #CSV file name
    v = float(sys.argv[1])             #v
    p = float(sys.argv[2])             #p

    #data = extract_data(file_name)
    #/mean = data[0]
    # std_deviation = data[1]

    import numpy as np
    mean = np.random.random(1000).tolist()
    std_deviation = np.abs(2+np.random.random(1000)).tolist()

    solve_cplex(mean, std_deviation, v, p)

