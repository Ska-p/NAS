import math
import random
import numpy as np
import matplotlib.pyplot as plt

true_mean = 0.5
true_var = 1/12
var_error = list()

n_list = [10, 100, 1000, 10000, 100000]

def generate_data(n_var,p):
    #Generate n iid U(0,1) variables
    rnd_vars = np.random.uniform(low=0, high=1, size=n_var)
    
    #Compute sample mean of a given vector of variables
    sample_mean = np.mean(rnd_vars)

    #Compute sample variance of a given vector of variables
    sample_var = np.var(rnd_vars)

    #Compute std dev
    sample_std_dev = np.std(rnd_vars)

    #Compute confidence intervals using bootstrap
    lower_ci , upper_ci = bootstrap_CI(rnd_vars, 25, 0.95)

    err = sample_var-lower_ci
    var_error.append((sample_var,err))

    #Compute prediction intervals using theory
    low_theory_PI, up_theory_PI = prediction_interval_theory(rnd_vars, 0.05)

    #Compute prediction intervals using bootstrap
    bs_pi = bs2(rnd_vars)

    return sample_mean, sample_var, lower_ci, upper_ci, low_theory_PI, up_theory_PI, bs_pi[0], bs_pi[1]

def bootstrap_CI(data, r0, gamma):

    #eventuale sistema se c'è tempo
    R =  np.ceil((2*r0)/(1-gamma))-1
    bootstrap_vars = []

    for i in range(int(R)):
        bootstrap_samples = np.random.choice(data, size=len(data), replace=True)
        bootstrap_var = np.var(bootstrap_samples)
        bootstrap_vars.append(bootstrap_var)

    sorted_vars = np.sort(bootstrap_vars)
    return sorted_vars[r0], sorted_vars[(int(R)+1)-r0]

def bs2(data):
    bootstrap_samples = []
    for i in range(1000):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_samples.append(bootstrap_sample)

    sorteddddd = np.sort(bootstrap_samples)
    lower_bound = np.percentile(sorteddddd, 2.5)
    upper_bound = np.percentile(sorteddddd, 97.5)

    return (lower_bound, upper_bound)


def prediction_interval_theory(data, alpha):
    sorted_data = np.sort(data)

    if(alpha>=(2/(len(sorted_data)+1))):
        low_PI = int(np.floor((n+1)*(alpha/2)))
        right_PI = int(np.ceil((n+1)*(1-(alpha/2))))
        return sorted_data[low_PI], sorted_data[right_PI]
    else:
        return sorted_data[0], sorted_data[len(sorted_data)-1]


for n in n_list:
    sample_mean, sample_var, lower_ci, upper_ci, low_theory_pi, up_theory_pi, low_bs_pi, up_bs_pi  = generate_data(n,p)
    sample_means.append(sample_mean)
    sample_vars.append(sample_var)
    print(f"Sample size: {n}")
    print(f"Sample mean: {sample_mean:.6f}")
    print(f"Sample variance: {sample_var:.6f}")
    print(f"Error in sample mean: {abs(sample_mean - true_mean):.6f}")
    print(f"Error in sample variance: {abs(sample_var - true_var):.6f}")
    print(f"Confidence intervals for the variance (using Bootstrap method):" "%.6f" % lower_ci, "%.6f" % upper_ci)
    print(f"95 Prediction intervals (using Theory): ", "%.6f"%low_theory_pi, "%.6f"%up_theory_pi)
    print(f"95 Prediction intervals (using bs): ", "%.6f"%low_bs_pi, "%.6f"%up_bs_pi)
    print("--------------")

fig, ax = plt.subplots(figsize=(8,5))
label=False
for sample in var_error:
    if(label==False):
        ax.errorbar(i, sample[0], yerr=sample[1], capsize=3, fmt='o', color='red', label='Variance CI')
        i+=1
        label=True
    else:
        ax.errorbar(i, sample[0], yerr=sample[1], capsize=3, fmt='o', color='red')
        i+=1

ax.set_xticks([0,1,2,3,4])
ax.set_xticklabels(['10','100','1000','10000','100000'])
ax.axhline((1/12),color='blue', linestyle="--", label="True value of variance")
ax.set_xlabel("Number of samples")
ax.set_ylabel("Value")
ax.legend()

plt.show()