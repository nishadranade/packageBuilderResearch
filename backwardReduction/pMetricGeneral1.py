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
        for j in distances[i]:
            if i == j:
                continue
            scenarioDist.add((distances[i][j], j))
        sortedDist.append(scenarioDist)
    return sortedDist

# method to eliminate a single scenario
def eliminate(scenarios, sortedList):



# method to redistribute the probabilities and fixing the distances matrix, SortedList after elimination
def redistribute(scenarios, sortedDist, dsitances):
    