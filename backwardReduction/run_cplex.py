# from super import*
from exactCplex import*
from scenarioGeneral import*
from pMetricGeneral3 import*
from generator import*
import sys
import time

def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    k = int(sys.argv[3])
    v = float(sys.argv[4])
    p = float(sys.argv[5])
    input_file = sys.argv[6]
    method = sys.argv[7]
    seed = int(sys.argv[8])

    assert 0 <= p <= 1
    assert n >= 1
    assert m >= 1

    mean, std_dev = extract_data(input_file)

    assert len(mean) == n
    assert len(std_dev) == n

    start_time = time.time()

    if method == "exact":
        # Run exact
        var_vals, obj_vals = solve_exact_cplex(mean, std_dev, v, p)
    elif method == "scenarios":
        values, distances, probs = generateMatrix(n, m, mean, std_dev, seed)
        new_m = m - k
        probs,distances,values,removed = eliminate_K(probs,distances,k,values)
        var_vals, obj_vals = solve_scenario_cplex(v, p, n, new_m, values, probs, mean)

    end_time = time.time()

    #should store in file including the input
    #output file must have format that have arguments and outputs, start times, end times
    print(var_vals)
    print(obj_vals)

    file = open("test_n={}_{}.txt".format(n, method), "w")
    file.writelines("n = {}\n".format(n))
    file.writelines("m = {}\n".format(m))
    file.writelines("k = {}\n".format(k))
    file.writelines("v = {}\n".format(v))
    file.writelines("p = {}\n".format(p))
    file.writelines("method: {}\n\n".format(method))
    file.writelines("mean: {}\n\n".format(mean))
    file.writelines("std_dev: {}\n\n".format(std_dev))
    file.writelines("CPLEX solution values: {}\n\n".format(var_vals))
    file.writelines("CPLEX solution objective value: {}\n\n".format(obj_vals))
    file.write("Runtime: {}\n".format(end_time-start_time))
    file.close()



if __name__ == "__main__":
    main()