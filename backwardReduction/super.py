from generator import *
from pMetricGeneral3 import *
from scenarioGeneral import *
import copy

# n and m are passed in

# generate m samples each of n normal distributions
# means and std dev for each can be generated by another distribution

def reductionStage(n, m):
    values, distances, means, std_devs, probs = generateMatrix(n, m)    #generateMatrix( ) has additional arguments: means, std_devs, seed

    #store a copy of values, distances
    original_values = copy.deepcopy(values)
    original_distances = copy.deepcopy(distances)
    original_probs = copy.deepcopy(probs)
    original_means = copy.deepcopy(means)
    original_std_devs = copy.deepcopy(std_devs)


    #assume that we are going to remove m/2 scenarios for now
    n_removed = m//2
    new_m = m - n_removed
    probs,distances,values,removed = eliminate_K(probs,distances,n_removed,values)

    # update the means and standard deviation
    for i in reversed(range(0, len(original_means))):
        if i in removed:
            np.delete(means, i)
            np.delete(std_devs, i)
    # temporary
    v = 10
    p = 0.99

    var_vals, obj_vals = solve_scenario_cplex(v, p, n, new_m, values, probs, means)

    print(var_vals)
    print(obj_vals)   



if __name__=="__main__":
    reductionStage(10, 100)  #first arg: n, second arg: m
    
