import numpy as np
import random
import cplex 
import scipy as sp

random.seed(100)

t = np.random.normal(0, 1, 3)
p = 0.9

# let us for simplicity assume that all t_i are std normal
# all x_i are binary


# let t_1 = (1, 1), t_2 = (2, 1), t_3 = (3, 1)
# v = 5

problem = cplex.Cplex()


names = ["x_1", "x_2", "x_3", "c"]

# names.append("c")

problem.variables.add( names=names)

problem.variables.set_types( [
    ("x_1", problem.variables.type.binary),
    ("x_2", problem.variables.type.binary),
    ("x_3", problem.variables.type.binary),
    ("c", problem.variables.type.continuous)        
])

objective = [ 1, 2, 3, 0]
problem.objective.set_sense(problem.objective.sense.minimize)
pairs = zip(names, objective)
problem.objective.set_linear(pairs)

# print(t)
lin_constraint = [["x_1", "x_2", "x_3", "c" ], [1, 2, 3, -1.285]]

problem.linear_constraints.add(lin_expr=[lin_constraint], rhs=[-1], senses='G')
# rhs = 5

constraint_senses = ["G"]

quad_constraint = cplex.SparseTriple(ind1 = ["x_1", "x_2", "x_3", "c" ], ind2= ["x_1", "x_2", "x_3", "c" ],
val = [1,1,1,-1])       

problem.quadratic_constraints.add(rhs = 0.0, quad_expr=quad_constraint, name="Q", sense='L')

problem.solve()

print(problem.solution.get_values())

print(problem.solution.get_objective_value())
