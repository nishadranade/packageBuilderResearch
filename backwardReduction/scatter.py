from generator import *
from pMetricGeneral3 import *
import sys
import numpy as np
from matplotlib import pyplot as plt


#scenarios_array_1 & scenarios_array_2: array of tuples 
def scatterPlot(scenarios_array_1, probability_1, scenarios_array_2, probability_2):

    x1 = [value[0] for value in scenarios_array_1]
    y1 = [value[1] for value in scenarios_array_1]

    x2 = [value[0] for value in scenarios_array_2]
    y2 = [value[1] for value in scenarios_array_2]

    plt.figure(figsize=[12, 6])     #figsize = [width, height]

    #Original Density Plot
    plt.subplot(1, 2, 1)
    plt.scatter(x1, y1, c=probability_1, s=50, edgecolors='')

    plt.title('Random var_1 vs. Random var_2')
    plt.xlabel('Random var_1')
    plt.ylabel('Random var_2')

    plt.xticks()
    plt.xticks(rotation=45, ha="right")
    plt.yticks()

    #Reduced Density Plot
    plt.subplot(1, 2, 2)
    plt.scatter(x2, y2, c=probability_2, s=50, edgecolors='')

    plt.title('Random var_1 vs. Random var_2')
    plt.xlabel('Random var_1')
    plt.ylabel('Random var_2')

    plt.xticks(rotation=45, ha="right")
    plt.yticks()
    #plt.savefig('plots/density{}.png'.format(1))
    plt.show()
    

#values: array of tuples 
def singleScatterPlot(values, probability, n, k, min_prob, max_prob):
    plt.clf()

    x = [value[0] for value in values]
    y = [value[1] for value in values]

    #min_p to max_p should be across plot 
    min_p = min_prob #np.min(probability)
    max_p = max_prob #np.max(probability)

    #for i from 0 to n
    for i in range(len(x)): 
        a = 2*probability[i] + 0.5
        if (max_p == min_p):
            a = 0.25
        else:
            a = ((probability[i]-min_p)*0.75)/(max_p - min_p) + 0.25       #maybe play with range with 0.25 to 1
        #NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        #print(a)
        plt.scatter(x[i], y[i], s=150*a, c='blue', edgecolors='', alpha=a) #c=probability #for loop probability and call scatter

    plt.title('{} Scenarios with {} Scenarios Reduced'.format(n, k))
    plt.xlabel('Random var_1')
    plt.ylabel('Random var_2')

    plt.xticks(rotation=45, ha="right")
    plt.yticks()
    plt.savefig('plots/n1-{}_k-{}_.png'.format(n, k))
    #plt.show()

        

if __name__=='__main__':
    array = [(10, 33), (45, 96), (63, 14), (12, 65), (66, 17), (53, 27), (38, 45)]
    #array = [(0.2, 0.5), (0.7, 0.3), (0.4, 0.1)]
    #singleScatterPlot(array)