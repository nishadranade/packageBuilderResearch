import numpy as np

#s = np.random.normal(10, 2.5, 11)
#d = np.random.randint(3, 12)

def generateScenarios(numVar):
    var = []
    for i in range(0, numVar):
        var.append([])
    for v in var:
        vals = np.random.randint(3,12)
        s = np.random.normal(10, 2.5, vals)
        sum1 = 0
        for i in range(0, len(s)):
            s[i] = abs(s[i])
            sum1 += s[i] 
        sum2 = 0
        for i in range(0, len(s)):
            s[i] = s[i]/sum1
            v.append(s[i])
            sum2 += s[i]
    return var

if __name__=="__main__":    
    dataset = generateScenarios(4)

    print('[')
    for i in dataset:
        print(str(i) + ',')
    print(']')
