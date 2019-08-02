import numpy as np

# Given the distances matrix, distance between every pair of scenarios
# Distance matrix will have reduntant data since distance is symmetric
# When a certain scenario is deleted, the corresponding row as well as column will be deleted
# The main method will call the following two methods k times in order to eliminate k scenarios

# method to choose one scenario to remove from the set
def eliminate(scenarios, distances):
    l1 = 100            #basically a large number
    index = -1          #a random index
    for i in range(0, len(scenarios)):
            if l1 > scenarios[i]*min(distances[i]):
                l1 = scenarios[i]*min(distances[i])
                index = i
    return scenarios, distances, index

# method to redistribute the probabilities of the remaining scenarios to add up to 1 again
def redistribute(scenarios, distances,index):
    closest = -1
    for i in range(0, len(scenarios)):
        if distances[index][i] == min(distances[index]):
            closest = i
    scenarios[closest] += scenarios[index]
    del scenarios[index]
    del distances[index]
    for row in distances:
        del row[index]
    return scenarios, distances

# method to eliminate k scenarios, one at a time
def deleteK(scenarios, distances, k):
    a = []
    for i in range(0,k):
        a = eliminate(scenarios, distances)
        a = redistribute(a[0], a[1], a[2])
        scenarios = a[0]
        distances = a[1]
    return scenarios, distances

if __name__ == '__main__':
    # given list of scenarios 
    scenarios = [ 0.2, 0.3, 0.1, 0.4]
    distances = [[100, 11, 12, 13], [11, 100, 4, 5], [12, 4, 100, 6], [13, 5, 6, 100]]
    print(deleteK(scenarios, distances, 2))