import sys
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import gaussian_kde

#scenarios_array_1 & scenarios_array_2: array of tuples 
def scatterPlot(scenarios_array_1, scenarios_array_2):

    x1 = [value[0] for value in scenarios_array_1]
    y1 = [value[1] for value in scenarios_array_1]

    x2 = [value[0] for value in scenarios_array_2]
    y2 = [value[1] for value in scenarios_array_2]

    #Calculate density of x and y
    stacked_xy1 = np.vstack([x1, y1])
    density_1 = gaussian_kde(stacked_xy1)(stacked_xy1)

    stacked_xy2 = np.vstack([x2, y2])
    density_2 = gaussian_kde(stacked_xy2)(stacked_xy2)

    plt.figure(figsize=[12, 6])     #figsize = [width, height]

    #Original Density Plot

    plt.subplot(1, 2, 1)
    plt.scatter(x1, y1, c=density_1, s=50, edgecolors='')

    plt.title('Random var_1 vs. Random var_2')
    plt.xlabel('Random var_1')
    plt.ylabel('Random var_2')

    plt.xticks()
    plt.xticks(rotation=45, ha="right")
    plt.yticks()

    #Reduced Density Plot

    plt.subplot(1, 2, 2)
    plt.scatter(x2, y2, c=density_2, s=50, edgecolors='')

    plt.title('Random var_1 vs. Random var_2')
    plt.xlabel('Random var_1')
    plt.ylabel('Random var_2')

    plt.xticks()
    plt.xticks(rotation=45, ha="right")
    plt.yticks()

    plt.show()

#scenarios_array: array of tuples 
def singleScatterPlot(scenarios_array):

    #plt.ion()

    x = [value[0] for value in scenarios_array]
    y = [value[1] for value in scenarios_array]

    #Calculate density of x and y
    stacked_xy = np.vstack([x, y])
    density = gaussian_kde(stacked_xy)(stacked_xy)

    #Sort points by density so that the most dense points are plotted on top
    #Only works for integer array
    # idx = density.argsort()
    # x = x[idx]
    # y = y[idx]
    # density = density[idx] 

    plt.scatter(x, y, c=density, s=50, edgecolors='')

    plt.title('Random var_1 vs. Random var_2')
    plt.xlabel('Random var_1')
    plt.ylabel('Random var_2')

    plt.xticks()
    plt.xticks(rotation=45, ha="right")
    plt.yticks()

    #plt.show(block=True)
    
    plt.show()

    #plt.pause(3)


if __name__=='__main__':
    array = [(10, 33), (45, 96), (63, 14), (12, 65), (66, 17), (53, 27), (38, 45)]
    #array = [(0.2, 0.5), (0.7, 0.3), (0.4, 0.1)]
    singleScatterPlot(array)