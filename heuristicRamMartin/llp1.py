import cplex

problem = cplex.Cplex()

problem.objective.set_sense(problem.objective.sense.minimize)

# 12 variables, p1-p6 for the new probabilities to be assigned, 
# w1-w6 each representing the presence of a certain scenario in the new set

names = ["p1","p2","p3","p4","p5","p6","w1","w2","w3","w4","w5","w6"]

# objective = w1 + w2 + w3 + w4 + w5 + w6
objective = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# the probabilities are between 0 and 1, while w1-6 are later cast as binary, so
# the upper bound does not matter
lower_bounds = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0]
upper_bounds = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2, 2, 2, 2, 2, 2]

# set objective
problem.variables.add( obj = objective, lb=lower_bounds, ub=upper_bounds, names=names)

# set the types of variables p1-p6 as continuous, and w1-w6 as binary
problem.variables.set_types([ ("p1", problem.variables.type.continuous),
                              ("p2", problem.variables.type.continuous),
                              ("p3", problem.variables.type.continuous),
                              ("p4", problem.variables.type.continuous),
                              ("p5", problem.variables.type.continuous),
                              ("p6", problem.variables.type.continuous),  
                            ("w1", problem.variables.type.binary),
                            ("w2", problem.variables.type.binary),
                            ("w3", problem.variables.type.binary),
                            ("w4", problem.variables.type.binary),
                            ("w5", problem.variables.type.binary),
                            ("w6", problem.variables.type.binary)])


# 12 constraints, one for each original probability (5), one for the sum to be 1,
# and 6 for the presence variable being greater than or equal to its probability
 
constraint_names = ["s1","s2","s3","s4","s5", "summation", "q1", "q2","q3","q4","q5","q6"]

# p1 + p2 + p3 = 0.7
first_constraint = [["p1","p2","p3","p4","p5","p6","w1","w2","w3","w4","w5","w6"],
                    [1.0,1.0,1.0,0, 0, 0, 0, 0, 0, 0, 0, 0]]

second_constraint = [[3,4,5],[1,1,1]]
third_constraint = [[0,3],[1,1]]
fourth_constraint = [ [1,4], [1,1]]
fifth_constraint = [[2,5], [1,1]]
sixth_constraint = [[0,1,2,3,4,5], [1,1,1,1,1,1]]
seventh_constraint = [[0,6], [1, -1]]
eighth_constraint = [ [1,7], [1,-1]]
ninth_constraint = [[2,8], [1, -1]]
tenth_constraint = [[3, 9], [1, -1]]
eleventh_constraint = [[4,10], [1,-1]]
twelfth_constraint = [[5,11], [1, -1]]

rhs = [0.4, 0.6, 0.2, 0.35, 0.45, 1.0, 0, 0, 0, 0, 0, 0]

constraint_senses = ["EEEEEELLLLLL"]

constraints = [first_constraint, second_constraint, third_constraint, fourth_constraint,
            fifth_constraint, sixth_constraint, seventh_constraint, eighth_constraint,
            ninth_constraint, tenth_constraint, eleventh_constraint, twelfth_constraint]

problem.linear_constraints.add(lin_expr= constraints, 
    senses=constraint_senses, 
    rhs = rhs, 
    names = constraint_names )

print(problem.variables.get_names)
#print(problem.objective.get_linear())

#print(problem.linear_constraints.get_rows() )

problem.solve()

print(problem.solution.get_values())

print(problem.solution.get_objective_value())
