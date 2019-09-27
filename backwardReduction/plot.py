import sys
import numpy as np
from matplotlib import pyplot as plt

input = sys.argv[1]

with open(input) as file:
    data = file.read()

data = data.split('\n')

numScenario = [float(row.split(', ')[0]) for row in data]

numScenarioEliminated = [float(row.split(', ')[1]) for row in data]

time = [float(row.split(', ')[2]) for row in data]


numScenario_max = max(numScenario)
numScenario_min = min(numScenario)
numScenario_interval = numScenario_max//len(numScenario)

numScenarioEliminated_max = max(numScenarioEliminated)
numScenarioEliminated_min = min(numScenarioEliminated)
numScenarioEliminated_interval = numScenarioEliminated_max//len(numScenarioEliminated)

time_max = max(time)
time_min = min(time)
time_interval = time_max//len(time)

# Number of Scenarios vs. Time
plt.subplot(2, 2, 1)
plt.scatter(numScenario, time)
plt.plot(numScenario, time)

plt.title('Number of Scenarios vs. Time')
plt.xlabel('Number of Scenarios')
plt.ylabel('Time (s)')
plt.xticks(np.arange(0, 1.5*numScenario_max, numScenario_interval)) 
plt.xticks(rotation=45, ha="right")
plt.yticks(np.arange(0, 1.5*time_max, time_interval))
#plt.yticks(rotation=45, ha="right")
#plt.axis([numScenario_min, numScenario_max, time_min, time_max])
plt.grid()
#plt.show()


# Number of Scenarios Eliminated vs. Time
plt.subplot(2, 2, 2)
plt.scatter(numScenarioEliminated, time)
plt.plot(numScenarioEliminated, time)
plt.title('Number of Scenarios Eliminated vs. Time')
plt.xlabel('Number of Scenarios Eliminated')
plt.ylabel('Time (s)')
plt.xticks(np.arange(0, 1.5*numScenarioEliminated_max, numScenarioEliminated_interval))
plt.xticks(rotation=45, ha="right")
plt.yticks(np.arange(0, 1.5*time_max, time_interval))
#plt.yticks(rotation=45, ha="right")
#plt.axis([numScenarioEliminated_min, numScenarioEliminated_max, time_min, time_max])
plt.grid()

plt.show()


