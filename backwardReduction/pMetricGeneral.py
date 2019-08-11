# Optimized implementation of Backward Reduction
# Store the distances in a list of heaps
# Need to somehow store the indexes from the distances matrix in the same order as the heap, so that removing and changing distances matrix is easy
# Data structures to use - Priority queue? x

# use sorted list - make a list of pairs - (distance, index), and sort based on distances
# ignore a scenario when storing corresponding sorted list since the indexes are already part of the tuple
# put results in a file

from sortedcontainers import SortedList

# method to create the presorted SortedLists based on distances for every scenario 
def preSort(scenarios, distances):
    sortedDist = []
    for i in range(0, len(scenarios)):
        scenarioDist = SortedList()
        for j in range(0, len(distances[i])):
            if i == j:
                continue
            scenarioDist.add((distances[i][j], j))
        sortedDist.append(scenarioDist)
    return sortedDist

# method to eliminate a single scenario
def eliminate(scenarios, sortedDist):
    rem = float('inf')
    index = -1
    for i in range(0, len(scenarios)):
        if sortedDist[i][0][0] * scenarios[i] < rem:
            rem = sortedDist[i][0][0] * scenarios[i]
            index = i 
    return index


# method to redistribute the probabilities and fixing the SortedLists after elimination
# the distances matrix is not adjusted here, since it is not needed once the SortedLists are made
# the scenarios[index] is set to infinity, and not removed completely because removing elements from the scenarios list will render the pre-sort useless,
# since the indices of scenarios will shift
def redistribute(index, scenarios, sortedDist):
    closestIndex = sortedDist[index][0][1]
    scenarios[closestIndex] += scenarios[index]
    for sortedList in sortedDist:
        for i in range(0, len(sortedList)):
            if sortedList[i][1] == index:
                sortedList.pop(i)
                break
    scenarios[index] = float('inf')
    return scenarios, sortedDist


# method to eliminate k scenarios, one at a time
def eliminateK(scenarios, distances, k):
    sortedDistances = preSort(scenarios, distances)
    for i in range(0, k):
        index = eliminate(scenarios, sortedDistances)
        result = redistribute(index, scenarios, sortedDistances)    
        scenarios = result[0]
        #distances = result[1]
        sortedDistances = result[1]
    for i in reversed(range(0, len(scenarios))):
        if scenarios[i] == float('inf'):
            scenarios.pop(i)
            for row in distances:
                del row[i]
            del distances[i]
    return scenarios, distances


# not called generally, only to test the file individually
if __name__ == '__main__':
    # given list of scenarios 
    scenarios = [ 0.2, 0.3, 0.1, 0.4]
    distances = [[0, 11, 12, 13], [11, 0, 4, 5], [12, 4, 0, 6], [13, 5, 6, 0]]
    print(eliminateK(scenarios, distances, 2))
