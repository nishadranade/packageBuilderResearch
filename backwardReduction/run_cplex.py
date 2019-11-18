# from super import*
from exactCplex import*
from scenarioGeneral import*
from pMetricGeneral3 import*
from generator import*
import sys
import time
from matplotlib import pyplot as plt

def run(n, m, k, v, p, input_file, method, seed):
    # n = int(sys.argv[1])
    # m = int(sys.argv[2])
    # k = int(sys.argv[3])
    # v = float(sys.argv[4])
    # p = float(sys.argv[5])
    # input_file = sys.argv[6]
    # method = sys.argv[7]
    # seed = int(sys.argv[8])

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
    run_time = end_time - start_time    #need to recompute run_time correctly for scenarios case

    #should store in file including the input
    #output file must have format that have arguments and outputs, start times, end times
    print(var_vals)
    print(obj_vals)

    write_to_file(n, m, k, v, p, method, mean, std_dev, var_vals, obj_vals, run_time)

    return obj_vals, run_time

def write_to_file(n, m, k, v, p, method, mean, std_dev, var_vals, obj_vals, run_time):
    file = open("CPLEX Tests/test_n={}_m={}_k={}_{}.txt".format(n, m, k, method), "w")
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
    file.writelines("Runtime: {}\n".format(run_time))
    file.close()

def plot(n, m, v, p, input_file, seed):
    
    exact_result = run(n, m, 0, v, p, input_file, "exact", seed)

    scenarios_obj_vals = []
    scenarios_time = []
    k = []

    for i in range(0, m, m//10):
        k.append(i)
        scenarios_result = run(n, m, i, v, p, input_file, "scenarios", seed)
        scenarios_obj_vals.append(scenarios_result[0])
        scenarios_time.append(scenarios_result[1])
    

    size = len(scenarios_obj_vals)      #to have the same number of elements for exact_obj_vals and exact_time as that of scenarios_obj_vals and scenarios_time

    exact_obj_vals = [exact_result[0]] * size
    exact_time = [exact_result[1]] * size

    print('exact_obj_vals {}'.format(exact_obj_vals))
    print('exact_time {}'.format(exact_time))
    print('scenarios_obj_vals {}'.format(scenarios_obj_vals))
    print('scenarios_time {}'.format(scenarios_time))           

    #Obj_vals vs. k
    plt.subplot(1, 2, 1)
    plt.scatter(k, exact_obj_vals)
    plt.plot(k, exact_obj_vals)

    plt.scatter(k, scenarios_obj_vals)
    plt.plot(k, scenarios_obj_vals)

    plt.legend(["Exact", "Scenarios"], loc='upper right')

    plt.title('Obj_vals vs. k')
    plt.xlabel('k')
    plt.ylabel('Objective Values')
    plt.xticks(rotation=45, ha="right")
    plt.yticks()
    plt.grid()

    #Times vs. k
    plt.subplot(1, 2, 2)
    plt.scatter(k, exact_time)
    plt.plot(k, exact_time)

    plt.scatter(k, scenarios_time)
    plt.plot(k, scenarios_time)

    plt.legend(["Exact", "Scenarios"], loc='upper right')

    plt.title('Time vs. k')
    plt.xlabel('k')
    plt.ylabel('Time')
    plt.xticks(rotation=45, ha="right")
    plt.yticks()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    k = int(sys.argv[3])
    v = float(sys.argv[4])
    p = float(sys.argv[5])
    input_file = sys.argv[6]
    method = sys.argv[7]
    seed = int(sys.argv[8])
    #run(n, m, k, v, p, input_file, method, seed)
    plot(n, m, v, p, input_file, seed)