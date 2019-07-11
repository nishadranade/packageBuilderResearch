import cplex
import numpy as np 

problem = cplex.Cplex()


problem.objective.set_sense(problem.objective.sense.minimize)

# checklist 
# objective size = 2*scenarios, with coefficients of the first s ones 0, and second s ones 1
# variables = size same as objective, half of them are ps, others ws
# constraints = number of vals + summation + scenarios (for the sum of ws)


# the input is a list of tuples, one tuple per variable, where the size of each tuple is the number of values
# that variable can take 
# for example: [[0.3, 0.4, 0.3], [0.5, 0.3, 0.1, 0.1], [0.35, 0.65]]
# or the one in llp1.py - [[0.7, 0.3], [0.1, 0.4, 0.5]]
# from the paper: [[0.2, 0.6, 0.2], [0.1, 0.7, 0.2]]
# from the paper: [[0.007, 0.1545, 0.677, 0.1545, 0.007], [0.007, 0.1545, 0.677, 0.1545, 0.007], [0.007, 0.1545, 0.677, 0.1545, 0.007]]
# initial input dataset
# [[0.10918825045332105, 0.1390662139850156, 0.1399467140895819, 0.12885230442211076, 0.07542377345339003, 0.11822901668003952, 0.08971036245167864, 0.0956943861502165, 0.10388897831464612],
# [0.23839515632393005, 0.3623178367322421, 0.3992870069438278],
# [0.08139295169575947, 0.12369209746033535, 0.14679552772247775, 0.11344157807855614, 0.08458066806043495, 0.15036191918741368, 0.17279146108792573, 0.12694379670709688],
# [0.17597892079106417, 0.2204223186665732, 0.12509211227139438, 0.14803444312802413, 0.16789867370137168, 0.1625735314415724],
# [0.36967879372820334, 0.24619999913660615, 0.38412120713519066],
# [0.18310126292034923, 0.1529079089265631, 0.14398244573615435, 0.09856141586119815, 0.20645747309184168, 0.21498949346389354],
# [0.08009033001858419, 0.13243658991514848, 0.11207183145912399, 0.08014378196987322, 0.10570414980812488, 0.10027564818019086, 0.1241840256488251, 0.07124646032927713, 0.08667548790082126, 0.10717169477003084],
# [0.28036493203188756, 0.12184249115678457, 0.20273330697873734, 0.20722300328151788, 0.18783626655107266],
# [0.17078891634564913, 0.47668529368750406, 0.35252578996684686],
# [0.24888436161577981, 0.2277626745589269, 0.06421226081869072, 0.16191629197826835, 0.16987185564387963, 0.12735255538445459]]



dataset = [[0.2, 0.3, 0.5], [0.3, 0.1, 0.4, 0.2], [0.6, 0.1, 0.1, 0.2]]
# number of variables
variablesTotal = len(dataset)

# number of values every variable takes
totalVals = 0
numVals = []

for v in dataset:
    numVals.append(len(v))
    totalVals = totalVals + len(v)

# the number of 'p's and 'w's is the total number of scenarios possible
# the total number of scenarios possible
scenarios = 1
for n in dataset:
    scenarios = scenarios*len(n)

#create a list of names, using a naming scheme that can be labeled using a loop
# have two numbers in the name- of the type a1b1 and w1x1 
pNames = []
wNames = []

# NUMBER OF VARIABLES = 2* SCENARIOS

for i in range(0, scenarios):
        pNames.append('p' + str(i))
        wNames.append('w' + str(i))

varNames = []
varNames.extend(pNames)
varNames.extend(wNames) 

pUpperBounds = []
pLowerBounds = []
wUpperBounds = []
wLowerBounds = []

lower_bounds = []
upper_bounds = []

# create separate lists for upper bounds for the p and w variables
# will be combined later to form two big upper and lower bounds list

for i in range(0, scenarios):
    pUpperBounds.append(1.0)
    pLowerBounds.append(0.0)
    wUpperBounds.append(2)
    wLowerBounds.append(0)

# final upper and lower bound lists created
lower_bounds.extend(pLowerBounds)
lower_bounds.extend(wLowerBounds)
upper_bounds.extend(pUpperBounds)
upper_bounds.extend(wUpperBounds)

# create a list for the objective:
objective = []

# add zeros for the first 'scenario' number of indices, ones for the rest
for i in range(0, 2*scenarios):
    if i < scenarios:
        objective.append(0)
    else: 
        objective.append(1)

problem.variables.add(obj=objective, lb=lower_bounds, ub=upper_bounds, names= varNames)

#   **********
#'p' + str(n) 
#for i in range(0, scenarios):
#    problem.variables.set_types(pNames[i], problem.variables.type.continuous)
#    problem.variables.set_types(wNames[i], problem.variables.type.binary)
# figure out a formula for the constraints , maybe consider renaming the variables 
# with two indices instead of just one 
# **************

# set types for each of the variable 
for i in range(0, scenarios):
    problem.variables.set_types(i, problem.variables.type.continuous)
    problem.variables.set_types(i+scenarios, problem.variables.type.binary)


# OBJECTIVE AND VARIABLES DONE , CONSTRAINTS START HERE

# number of constraint names = 1(zero) + totalVals + 1(summation) + scenarios
constraint_names = ['zero']
for i in range(0, totalVals):
    constraint_names.append('s' + str(i))

constraint_names.append('summation')

for i in range(0, scenarios):
    constraint_names.append('q' + str(i))

# constraint_names is taken care of for now, now the actual constraints
# make a list of tuples add directly add them so that you don't have to 
# name each one. 

# all variables and there values are stored in dataset[]
# numVals[] contains the number of values every variable can take

# consider a value(probability) aibj
# it appears in 

constraints = []
coefficients = []

rep = 1        # repeat consecutively        
for i in reversed(range(0, len(dataset))):
        #rep1 = 1        # repeat after
        for j in reversed(range(0, len(dataset[i]))):
                prob = dataset[i][j]
                indices = [] 
                # scenarios in which that specific value occurs
                occurrence = scenarios//(len(dataset[i]))
                actualOc = occurrence//rep
                for n in reversed(range(0, actualOc)):
                        step = rep*len(dataset[i])
                        for m in reversed(range(0, rep)):
                                #indices.insert(0, j*rep + len(dataset[i])*n + m + rep*n )
                                #indices.insert(0, j*rep + m + rep*n)
                                indices.insert(0, j*rep + step*n + m)
                coefficients.insert(0, indices)
        # calculate rep based on which variable from the end it is
        # product of variable values to its right
        rep = rep*len(dataset[i])

constraint_zero = []
conZeroNames = []
conZeroNames.extend(varNames)
constraint_zero.append(conZeroNames) 
constraint_zero.append( list(np.zeros(2*scenarios)))
constraints.append(constraint_zero)

# convert the list of indices to actual constraints by pairing them up with list of ones

for c in coefficients:
        pair = []
        pair.append(c)
        pair.append(list(np.ones(len(c))))
        constraints.append(pair)

# add the coefficients for the 'summation' constraint
# total number of all values = scenarios

summation = []
subSummation = []

for i in range(0, scenarios):
        subSummation.append(i)
summation.append(subSummation)
summation.append(list(np.ones(scenarios)))
constraints.append(summation)

# now add the last set of constraints -that the 'p's are always less than or equal to the ws
# there are a 'scenarios' number of constraints of this type with coef type i, i+scenarios

for i in range(0, scenarios):
        cons = []
        coef1 = []
        coef2 = [1 , -1]
        coef1.extend([i, i+scenarios])
        cons = [coef1, coef2]
        constraints.append(cons)

#print(len(constraints))
# for i in constraints:
#         print(i)

# Coefficients of all constraints are implemented
# rhs - totalsVals for the each of the probabilities, the next one is 1, and the rest, 0

rhs = [0]
for i in dataset:
        for j in i:
                rhs.append(j)

rhs.append(1.0)
rhs.extend(list(np.zeros(scenarios)))
 
#print(rhs, len(rhs))
constraint_senses = 'E'
for i in range(0, totalVals+1):
        constraint_senses = constraint_senses + 'E'

for i in range(0, scenarios):
        constraint_senses = constraint_senses + 'L'

constraint_senses = [constraint_senses]

#print(constraint_senses)
# # debugging
# for i in constraints:
#         print(i) 
# print(len(constraints))

problem.linear_constraints.add(lin_expr= constraints, 
    senses=constraint_senses, 
    rhs = rhs, 
    names = constraint_names )

# print(problem.variables.get_names)

# print(problem.objective.get_linear)
# print(problem.linear_constraints.get_rows)

problem.solve()

#print(problem.solution.get_values())
print(problem.solution.get_objective_value())

