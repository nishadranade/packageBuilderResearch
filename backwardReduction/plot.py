import sys
import numpy as np
from matplotlib import pyplot as plt

input = sys.argv[1]

with open(input) as file:
    data = file.read()

data = data.split('\n')

x = [int(row.split(', ')[0]) for row in data]

y = [int(row.split(', ')[2]) for row in data]

#dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#dev_y = [38496, 42000, 46752, 49320, 53200,
#         56000, 62316, 64928, 67317, 68748, 73752]

x_max = max(x)
x_min = min(x)
x_interval = x_max//len(x)

y_max = max(y)
y_min = min(y)
y_interval = y_max//len(y)

plt.scatter(x, y)

plt.plot(x, y)

plt.title('Number of Scenarios vs. Time')

plt.xlabel('Number of Scenarios')

plt.ylabel('Time (s)')

#plt.xticks(np.arange(0, x_max, x_interval)) 

#plt.yticks(np.arange(0, y_max, y_interval))

plt.grid()

plt.axis([x_min, x_max, y_min, y_max])

plt.show()

