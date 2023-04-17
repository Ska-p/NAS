import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def simulations(n_var,n_sim):

    confidence=list()

    for i in range(n_sim):

        #Generate n iid N(0,1) variables
        rnd_vars = np.random.normal(loc=0, scale=1, size=n_var)
    
        #Compute sample mean of a given vector of variables
        sample_mean = np.mean(rnd_vars)
    
        #Compute sample std_dev of a given vector of variables
        sample_std_dev = np.std(rnd_vars, ddof=1)

        #Compute the Confidence Interval bounds for the sample_mean
        ci = norm.interval(confidence=0.95, loc=sample_mean, scale=sample_std_dev/np.sqrt(n_var))

        #Compute error, used later in error bar plotting
        error = sample_mean - ci[0]
        
        if(ci[0] > 0 or ci[1] < 0):
            confidence.append((ci[0], ci[1], sample_mean, error, 1))
        else:
            confidence.append((ci[0], ci[1], sample_mean, error, 0))

    return confidence

#Order by lower bound
def lower_bound(tmp):
    return tmp[0]

#Run simulation 1000 times and each time generate 48 variables
data = simulations(48,1000)
data.sort(key=lower_bound)

#Plot confidence intervals
plt.figure(figsize=(12,5))

label_red = False
label_green = False
for sample in data:
    if(sample[4] == 1 and label_red==False):
        plt.errorbar(sample[0],sample[2], yerr=sample[3], color='red', label='Mean outside CI')
        label_red=True
    elif (sample[4] == 0 and label_green==False):
        plt.errorbar(sample[0],sample[2], yerr=sample[3], color='green',  label='Mean inside CI')
        label_green=True
    elif (sample[4] == 1 and label_red==True):
        plt.errorbar(sample[0],sample[2], yerr=sample[3], color='red')
    elif (sample[4] == 0 and label_green==True):
        plt.errorbar(sample[0],sample[2], yerr=sample[3], color='green')

plt.axhline(y=0, color='blue', linestyle='dotted', xmin=0, xmax=1, linewidth=1, label='Mean')
plt.xlabel("Confidence Interval's Lower Bound")
plt.ylabel("Values")
plt.legend(loc='upper left')
plt.show()