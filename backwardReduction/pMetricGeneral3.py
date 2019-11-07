# Optimized implementation of Backward Reduction
# Need to somehow store the indexes from the distances matrix in the same order as the heap, so that removing and changing distances matrix is easy
# use sorted list - make a list of pairs - (distance, index), and sort based on distances
# ignore a scenario when storing corresponding sorted list since the indexes are already part of the tuple
# put results in a file (do in terminal eg python run.py 100 20 >output.txt)
from scatter import scatterPlot
from sortedcontainers import SortedList
import numpy as np
# method to create the presorted SortedLists based on distances for every scenario

# instead of updating the SortedLists, use counters (one counter per SortedList) as well as a single universal Python set to document which indices
# have been eliminated. If works, uses same amount of space, but O(n) instead of O(n^2)

# removed = set()

# temporary method for asserting sums of redistributed scenario probabilites is 1
def sumN(scenarios):
    sum = 0
    for i in scenarios:
        if i <= 1:
            sum += i
    return sum

def preSort(scenarios, distances):
    removed = set()
    sortedDist = []
    counter = []
    for i in range(0, len(scenarios)):
        scenarioDist = SortedList()
        for j in range(0, len(distances[i])):
            if i == j:
                continue
            scenarioDist.add((distances[i][j], j))
        sortedDist.append(scenarioDist)
        counter.append(0)
    return sortedDist, counter, removed

# method to eliminate a single scenario
def eliminate(scenarios, sortedDist, counter, removed):
    rem = float('inf')
    index = -1
    for i in range(0, len(scenarios)):
        if i not in removed and sortedDist[i][counter[i]][0] * scenarios[i] < rem:
            rem = sortedDist[i][counter[i]][0] * scenarios[i]
            index = i
    return index


# method to redistribute the probabilities and fixing the SortedLists after elimination
# the distances matrix is not adjusted here, since it is not needed once the SortedLists are made
# the scenarios[index] is set to infinity, and not removed completely because removing elements from the scenarios list will render the pre-sort useless,
# since the indices of scenarios will shift
def redistribute(index, scenarios, sortedDist, counter, removed):
    closestIndex = sortedDist[index][counter[index]][1]
    while closestIndex in removed:
        counter[index] += 1
        closestIndex = sortedDist[index][counter[index]][1]
    scenarios[closestIndex] += scenarios[index]
    removed.add(index)
    scenarios[index] = float('inf')
    for i in range(0, len(sortedDist)):
        while sortedDist[counter[i]][1] in removed:
            counter[i] += 1
    return scenarios, sortedDist, counter, removed


# method to eliminate k scenarios, one at a time
def eliminateK(scenarios, distances, k, values):
    pre = preSort(scenarios, distances)
    sortedDistances = pre[0]
    counter = pre[1]
    removed = pre[2]
    for i in range(0, k):
        index = eliminate(scenarios, sortedDistances, counter, removed)
        result = redistribute(index, scenarios, sortedDistances, counter, removed)
        scenarios = result[0]
        #print(sumN(scenarios))
        p = sumN(scenarios)
        assert round(p, 6) == 1, p
        sortedDistances = result[1]
        counter = result[2]
        removed = result[3]
        if i == k//4 or i == 3*k//4:
            valTemp = np.delete(values, list(removed), axis=0)
            scatterPlot(valTemp)


    for i in reversed(range(0, len(scenarios))):
        if scenarios[i] == float('inf'):
            scenarios.pop(i)
            for row in distances:
                del row[i]
            del distances[i]
            values = np.delete(values, i, axis=0)
    return scenarios, distances, values

# new method that copies eliminate k but also returns removed
def eliminate_K(scenarios, distances, k, values):
    pre = preSort(scenarios, distances)
    sortedDistances = pre[0]
    counter = pre[1]
    removed = pre[2]
    for i in range(0, k):
        index = eliminate(scenarios, sortedDistances, counter, removed)
        result = redistribute(index, scenarios, sortedDistances, counter, removed)
        scenarios = result[0]
        #print(sumN(scenarios))
        p = sumN(scenarios)
        assert round(p, 6) == 1, p
        sortedDistances = result[1]
        counter = result[2]
        removed = result[3]
        if i == k//4 or i == 3*k//4:
            valTemp = np.delete(values, list(removed), axis=0)
            scatterPlot(valTemp)


    for i in reversed(range(0, len(scenarios))):
        if scenarios[i] == float('inf'):
            scenarios.pop(i)
            for row in distances:
                del row[i]
            del distances[i]
            values = np.delete(values, i, axis=0)
    return scenarios, distances, values, removed




# not called generally, only to test the file individually
if __name__ == '__main__':
    # given list of scenarios
    # scenarios = [ 0.2, 0.3, 0.1, 0.3, 0.1]
    # distances = [[0, 11, 12, 13, 20], [11, 0, 4, 5, 21], [12, 4, 0, 6, 22], [13, 5, 6, 0, 23], [20, 21, 22, 23, 0 ]]

    scenarios = [0.0625, 0.0625, 0.125, 0.09375, 0.09375, 0.171875, 0.078125, 0.140625, 0.109375, 0.0625]
    # distances = [[0, 57.434675940199774, 27.0487999509335, 10.214249907856166, 49.01394972927098], [57.434675940199774, 0, 90.9579977534611, 78.0139459672789, 7.255618787653085], [27.0487999509335, 90.9579977534611, 0, 61.023832685952584, 61.93477714455797], [10.214249907856166, 78.0139459672789, 61.023832685952584, 0, 28.78863352209865], [49.01394972927098, 7.255618787653085, 61.93477714455797, 28.78863352209865, 0]]
    distances = [[0, 44.51037204867403, 14.123662907165167, 36.188932892464265, 60.57952720766243, 51.96575648526366, 82.03556351686126, 74.34732821138373, 13.341321627045335, 19.70061945175303], [44.51037204867403, 0, 18.786133361779044, 85.5332052277817, 47.12496422598768, 87.17966720630307, 76.99499204799007, 63.975804020417975, 69.2894592815611, 48.38245533616908], [14.123662907165167, 18.786133361779044, 0, 11.422608909464612, 85.53801192299302, 81.1090740849236, 37.324250205400766, 52.90043858828369, 69.33114426447821, 60.19782688101434], [36.188932892464265, 85.5332052277817, 11.422608909464612, 0, 30.080659103321683, 19.17673869436715, 21.32476830123327, 19.549443690261338, 88.40459488249918, 78.78322523416401], [60.57952720766243, 47.12496422598768, 85.53801192299302, 30.080659103321683, 0, 15.534444115572205, 54.946613356319666, 32.81157126684496, 8.228824751204773, 31.506150744245033], [51.96575648526366, 87.17966720630307, 81.1090740849236, 19.17673869436715, 15.534444115572205, 0, 11.215327444144398, 40.83753447437728, 11.002504322164846, 31.203702245142907], [82.03556351686126, 76.99499204799007, 37.324250205400766, 21.32476830123327, 54.946613356319666, 11.215327444144398, 0, 79.51421886498609, 57.013578633168514, 8.075671208669673], [74.34732821138373, 63.975804020417975, 52.90043858828369, 19.549443690261338, 32.81157126684496, 40.83753447437728, 79.51421886498609, 0, 38.39272486660715, 90.35516913231494], [13.341321627045335, 69.2894592815611, 69.33114426447821, 88.40459488249918, 8.228824751204773, 11.002504322164846, 57.013578633168514, 38.39272486660715, 0, 52.90407754758379], [19.70061945175303, 48.38245533616908, 60.19782688101434, 78.78322523416401, 31.506150744245033, 31.203702245142907, 8.075671208669673, 90.35516913231494, 52.90407754758379, 0]]

    print(eliminateK(scenarios, distances, 9))
