import sys
import numpy as np
from matplotlib import pyplot as plt

#input: filename from sys.argv[1]
def plotGraph(values):
    #input = sys.argv[1]

    # with open(input, 'r') as file:
    #     data = file.read()

    data = values.split('\n')
    data = data[:len(data)-1]           #when bash nScript.sh > outN.txt or kScript.sh > outK.txt, there is an extra line after the last line
    #print('Size: {}'.format(len(data)))

    numScenario = [int(row.split(', ')[0]) for row in data]

    numScenarioEliminated = [int(row.split(', ')[1]) for row in data]

    time = [float(row.split(', ')[2]) for row in data]


    # numScenario_max = max(numScenario)
    # numScenario_min = min(numScenario)
    # numScenario_interval = numScenario_max//len(numScenario)

    # numScenarioEliminated_max = max(numScenarioEliminated)
    # numScenarioEliminated_min = min(numScenarioEliminated)
    # numScenarioEliminated_interval = numScenarioEliminated_max//len(numScenarioEliminated)

    # time_max = max(time)
    # time_min = min(time)
    # time_interval = time_max//len(time)

    # Number of Scenarios vs. Time
    plt.subplot(1, 2, 1)
    plt.scatter(numScenario, time)
    plt.plot(numScenario, time)

    plt.title('Number of Scenarios vs. Time')
    plt.xlabel('Number of Scenarios')
    plt.ylabel('Time (s)')
    #plt.xticks(np.arange(0, 1.5*numScenario_max, numScenario_interval)) 
    plt.xticks()
    plt.xticks(rotation=45, ha="right")
    #plt.yticks(np.arange(0, 1.5*time_max, time_interval))
    plt.yticks()
    plt.grid()


    # Number of Scenarios Eliminated vs. Time
    plt.subplot(1, 2, 2)
    plt.scatter(numScenarioEliminated, time)
    plt.plot(numScenarioEliminated, time)
    plt.title('Number of Scenarios Eliminated vs. Time')
    plt.xlabel('Number of Scenarios Eliminated')
    plt.ylabel('Time (s)')
    #plt.xticks(np.arange(0, 1.5*numScenarioEliminated_max, numScenarioEliminated_interval))
    plt.xticks()
    plt.xticks(rotation=45, ha="right")
    #plt.yticks(np.arange(0, 1.5*time_max, time_interval))
    plt.yticks()
    plt.grid()

    plt.show()

if __name__=='__main__':
    try:
        input = sys.argv[1]
        with open(input, 'r') as file:
            values = file.read()
    except IOError:
        print('Invalid File Name or File does not exist')
    plotGraph(values)

