import sys
import numpy as np
from matplotlib import pyplot as plt

#scenarios_array: array of tuples 
def scatterPlot(scenarios_array):

    x = [value[0] for value in scenarios_array]
    y = [value[1] for value in scenarios_array]

    plt.scatter(x, y, c='royalblue')

    plt.title('Random var_1 vs. Random var_2')
    plt.xlabel('Random var_1')
    plt.ylabel('Random var_2')

    plt.xticks()
    plt.xticks(rotation=45, ha="right")
    plt.yticks()

    plt.show()



if __name__=='__main__':
    array = [(10, 33), (45, 96), (63, 14), (12, 65), (66, 17), (53, 27), (38, 45)]
    #array = [(0.2, 0.5), (0.7, 0.3), (0.4, 0.1)]
    scatterPlot(array)