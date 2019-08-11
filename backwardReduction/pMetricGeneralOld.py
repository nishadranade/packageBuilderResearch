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

# not called generally, only to test the file individually
if __name__ == '__main__':
    # given list of scenarios 
    scenarios = [ 0.2, 0.3, 0.1, 0.4]
    # scenarios = [0.136986301369863, 0.1506849315068493, 0.0547945205479452, 0.1232876712328767, 0.1095890410958904, 0.0684931506849315, 0.1095890410958904, 0.0821917808219178, 0.0547945205479452, 0.1095890410958904]
    distances = [[100, 11, 12, 13], [11, 100, 4, 5], [12, 4, 100, 6], [13, 5, 6, 100]]
    # distances = [[0, 81.9611299351956, 12.159154172487085, 5.827533791522434, 50.150458702739066, 21.902315635983285, 28.783791423368786, 72.23785363032802, 75.91332794294699, 91.85887634739576],
    # [81.9611299351956, 0, 38.30701055981729, 72.23836554546916, 54.98991099326739, 46.79121004907131, 89.65601914170233, 50.554330141559156, 28.34961001372081, 35.75937560634261],
    # [12.159154172487085, 38.30701055981729, 0, 89.07921360033183, 4.236115458257038, 51.56762307098118, 98.5411660363732, 19.573170708714187, 48.222496947157175, 12.176054484356865],
    # [5.827533791522434, 72.23836554546916, 89.07921360033183, 0, 42.78631050409607, 30.24628024917142, 77.68318296035514, 69.4804572873154, 22.432437263930193, 90.77463332725262],
    # [50.150458702739066, 54.98991099326739, 4.236115458257038, 42.78631050409607, 0, 98.24795854708304, 10.229893866088407, 77.03924926705628, 86.30240967784376, 34.44570590692546],
    # [21.902315635983285, 46.79121004907131, 51.56762307098118, 30.24628024917142, 98.24795854708304, 0, 90.7307016695562, 75.17060009285088, 5.680413511295663, 31.214252576476483],
    # [28.783791423368786, 89.65601914170233, 98.5411660363732, 77.68318296035514, 10.229893866088407, 90.7307016695562, 0, 67.54564145063677, 63.54534848128776, 17.37223041227541],
    # [72.23785363032802, 50.554330141559156, 19.573170708714187, 69.4804572873154, 77.03924926705628, 75.17060009285088, 67.54564145063677, 0, 11.199720920908707, 85.8420915182568],
    # [75.91332794294699, 28.34961001372081, 48.222496947157175, 22.432437263930193, 86.30240967784376, 5.680413511295663, 63.54534848128776, 11.199720920908707, 0, 56.135163820438585],
    # [91.85887634739576, 35.75937560634261, 12.176054484356865, 90.77463332725262, 34.44570590692546, 31.214252576476483, 17.37223041227541, 85.8420915182568, 56.135163820438585, 0]]    
    print(deleteK(scenarios, distances, 2)[0])