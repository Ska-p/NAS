import math
from random import sample
import numpy as np
import matplotlib.pyplot as plt

def simulations(n_var,n_sim):

    confidence=list()

    for i in range(n_sim):
        #Generate n iid U(0,1) variables
        rnd_vars = np.random.uniform(low=0, high=1, size=n_var)
    
        #Compute sample mean of a given vector of variables
        sample_mean = np.mean(rnd_vars)
    
        #Compute sample std_dev of a given vector of variables
        sample_std_dev = np.std(rnd_vars)

        #Compute the sample error
        error = 1.96 * (sample_std_dev/(math.sqrt(len(rnd_vars))))

        #Compute the Confidence Interval bounds for the sample_mean
        lower_bound = sample_mean - error
        upper_bound = sample_mean + error
        
        #Check wether the true mean is contained in the CI
        if(lower_bound > 0.5 or upper_bound < 0.5):
            confidence.append((lower_bound, upper_bound, sample_mean, error, 1))
        else:
            confidence.append((lower_bound, upper_bound, sample_mean, error, 0))

    return confidence

#Function to order CI based on lower bound
def lower_bound_order(tmp):
    return tmp[0]

#Run the simulation 1000 times and each time generate 48 variables
data = simulations(48,1000)
data.sort(key=lower_bound_order)

#Plot the confidence intervals
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

plt.axhline(y=0.5, color='blue', linestyle='dotted', xmin=0, xmax=1, linewidth=1, label='Mean')
plt.xlabel("Confidence Interval's Lower Bound")
plt.ylabel("Values")
plt.legend(loc='upper left')
plt.show()