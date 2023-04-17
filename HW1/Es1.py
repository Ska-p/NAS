import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data = []

file = open(r"C:\Users\miche\Desktop\Uni\Network Analysis and Simulation\Homeworks\HW1\Data\figure 2.1\sgbdnew.dat", "r")
for line in file:
    data.append(line)
new_data = np.array(data, dtype='float')

file = open(r"C:\Users\miche\Desktop\Uni\Network Analysis and Simulation\Homeworks\HW1\Data\figure 2.1\sgbdold.dat", "r")
data = []
for line in file:
    data.append(line)
old_data = np.array(data, dtype='float')

file = open(r"C:\Users\miche\Desktop\Uni\Network Analysis and Simulation\Homeworks\HW1\Data\figure 2.10\joe.dat", "r")
data = []
for line in file:
    data.append(line)
joe_data = np.array(data, dtype='float')

#Plot of Figure 2.1
def fig21():
    
    fig, ax = plt.subplots(2,2, figsize=(10,10))
        
    #Red o datagram
    ax[0,1].set(xlabel="Transactions", ylabel="Execution Time [ms]", title="(b) Raw Data, New", ylim=(0,200), xlim=(0,100))
    ax[0,1].plot(np.arange(100), new_data, 'ro', fillstyle='none')
    ax[0,1].set_yticks(np.arange(0,250,50))

    #Blue + datagram
    ax[0,0].set(xlabel="Transactions", ylabel="Execution Time [ms]", title="(a) Raw Data, Old", ylim=(0,200), xlim=(0,100))
    ax[0,0].plot(np.arange(100), old_data, 'b+', fillstyle='none')
    ax[0,0].set_yticks(np.arange(0,250,50))

    #Red o histogram
    ax[1,1].set(title="(d) Histogram, New", xlabel="Execution Time [ms]", ylabel = "Value",  ylim=(0,35), xlim=(0,200))
    ax[1,1].hist(new_data, bins=[0,19.3,38,57,76,95,114,133,152,171,190], edgecolor='white', color='darkblue', rwidth=0.9)

    #Blue + histogram
    ax[1,0].set(title="(c) Histogram, Old", xlabel="Execution Time [ms]", ylabel = "Value", ylim=(0,25), xlim=(0,200))
    ax[1,0].hist(old_data, bins=[0,19.3,38,57,76,95,114,133,152,171,190], edgecolor='white', color='darkblue', rwidth=0.9)

#Plot of figure 2.2
def fig22():
    new_ecdf = np.sort(new_data)
    old_ecdf = np.sort(old_data)

    y_new = np.arange(1, len(new_data) + 1)/(len(new_data))
    y_old = np.arange(1, len(old_data) +1)/(len(old_data))

    plt.figure(figsize=(12,6))
    plt.plot(new_ecdf, y_new, color="red", linestyle="solid", label="New configuration")
    plt.plot(old_ecdf, y_old, color="darkblue", linestyle="solid", label="Old configuration")
    plt.xlim(0,200)
    plt.ylim(0,1)
    plt.xlabel("Execution Time [ms]")
    plt.legend(loc="upper left")

#Plot of figure 2.3
def fig23():
    
    both_data = [old_data, new_data]

    fig, ax = plt.subplots(1, 2, figsize=(12,5))
    ax[0].set_yticks(np.arange(0,250,50))
    ax[0].set_xticklabels(["Old", "New"])
    ax[0].set_ylabel("Value")
    bp = ax[0].boxplot(both_data, notch='true', sym="r+")

    for i in bp['fliers']:
        print(i.get_ydata())

    new_values = bp['boxes'][1].get_ydata()
    old_values = bp['boxes'][0].get_ydata()

    ax[0].axhline(y=old_values[3], color='red', linestyle='-', xmin=0.1, xmax=0.4, linewidth=1)
    ax[0].axhline(y=old_values[2], color='black', linestyle='dotted', xmin=0, xmax=0.5, linewidth=1, label='Median\s CI')
    ax[0].axhline(y=old_values[4], color='black', linestyle='dotted', xmin=0, xmax=0.5, linewidth=1)
    
    ax[0].axhline(y=new_values[3], color='red', linestyle='-', xmin=0.6, xmax=0.9, linewidth=1)
    ax[0].axhline(y=new_values[2], color='black', linestyle='dotted', xmin=0.5, xmax=1, linewidth=1)
    ax[0].axhline(y=new_values[4], color='black', linestyle='dotted', xmin=0.5, xmax=1, linewidth=1)
    
    hanl, labl = ax[0].get_legend_handles_labels()
    hanl.append(bp['medians'][0])
    hanl.append(bp['fliers'][0])
    labl.append('Median')
    labl.append('Outliers')
    ax[0].legend(hanl, labl, loc='upper right')


    ax[1].set_yticks(np.arange(0,250,50))
    ax[1].set_ylabel("Value")
    ax[1].set_xticklabels(["Old", "New"])
    bp = ax[1].boxplot(both_data, notch='true', sym="r+")

    sample_mean = np.mean(new_data)
    sample_std_dev = np.std(new_data, ddof=1)
    ci = 1.96 * (sample_std_dev/(math.sqrt(len(new_data))))
    lower_ci = sample_mean - ci
    upper_ci = sample_mean + ci
    ax[1].axhline(y=sample_mean, color='green', linestyle='-', xmin=0.6, xmax=0.9, linewidth=1)
    ax[1].axhline(y=lower_ci, color='green', linestyle='--', xmin=0.5, xmax=1, linewidth=1, label = "Means's CI" )
    ax[1].axhline(y=upper_ci, color='green', linestyle='--', xmin=0.5, xmax=1, linewidth=1)
    ax[1].axhline(y=(sample_mean + 1.96*sample_std_dev), color='k', linestyle='--', xmin=0.5, xmax=1, linewidth=1)
    ax[1].axhline(y=0, color='k', linestyle='--', xmin=0.5, xmax=1, linewidth=1)

    sample_mean = np.mean(old_data)
    sample_std_dev = np.std(old_data, ddof=1)
    ci = 1.96 * (sample_std_dev/(math.sqrt(len(old_data))))
    lower_ci = sample_mean - ci
    upper_ci = sample_mean + ci
    ax[1].axhline(y=sample_mean, color='green', linestyle='-', xmin=0.1, xmax=0.4, linewidth=1, label='Mean')
    ax[1].axhline(y=lower_ci, color='green', linestyle='--', xmin=0, xmax=0.5, linewidth=1)
    ax[1].axhline(y=upper_ci, color='green', linestyle='--', xmin=0, xmax=0.5, linewidth=1)
    ax[1].axhline(y=(sample_mean + 1.96*sample_std_dev), color='k', linestyle='--', xmin=0, xmax=0.5, linewidth=1, label='Prediction Interval')
    ax[1].axhline(y=0, color='k', linestyle='--', xmin=0, xmax=0.5, linewidth=1)
    hanl, labl = ax[1].get_legend_handles_labels()
    hanl.append(bp['medians'][0])
    hanl.append(bp['fliers'][0])
    labl.append('Median')
    labl.append('Outliers')
    ax[1].legend(hanl, labl, loc='upper right')

#Plot of figure 2.7
def fig27():

    reduction_time = old_data - new_data
    fig, ax = plt.subplots(1,3)
    
    #Left plot - Basic plot
    ax[0].plot(np.arange(0,100), reduction_time, "kx")
    ax[0].set_yticks(np.arange(-100,250,50))
    ax[0].set_xticks(np.arange(0,150,50))
    ax[0].set_ylabel("Reduction Time [ms]")
    ax[0].set_xlabel("Transactions")
    #Central plot - Hist plot
    ax[1].hist(reduction_time, edgecolor='black', color='darkblue')
    ax[1].set_xticks(np.arange(-100,250,50))
    ax[1].set_yticks(np.arange(0,35,5))
    ax[1].set_xlabel("Reduction Time [ms]")
    ax[1].set_ylabel("Value")

    #Right plot - Box plot
    bp = ax[2].boxplot(reduction_time, notch='true', sym="r+")
    ax[2].set_yticks(np.arange(-100,200,50))
    ax[2].set_ylabel("Value")

    #Compute confidence intervals for the mean
    sample_mean = np.mean(reduction_time)
    sample_std_dev = np.std(reduction_time, ddof=1)
    ci = 1.96 * (sample_std_dev/(math.sqrt(len(reduction_time))))
    lower_ci = sample_mean - ci
    upper_ci = sample_mean + ci
    
    #Add confidence intervals line and mean line to box plot
    ax[2].axhline(y=sample_mean, color='green', linestyle='-', xmin=0, xmax=1, linewidth=1, label='Mean')
    ax[2].axhline(y=lower_ci, color='green', linestyle='--', xmin=0, xmax=1, linewidth=1, label='Mean\'s CI')
    ax[2].axhline(y=upper_ci, color='green', linestyle='--', xmin=0, xmax=1, linewidth=1)
    
    #legend for box plot
    hanl, labl = ax[2].get_legend_handles_labels()
    hanl.append(bp['medians'][0])
    hanl.append(bp['fliers'][0])
    labl.append('Median')
    labl.append('Outliers')
    ax[2].legend(hanl, labl, loc='upper left')

#Plot of figure 2.8
def fig28():
    old_mean_exec_time = np.mean(old_data)
    new_mean_exec_time = np.mean(new_data)

    fig, ax = plt.subplots()
    #Confidence intervals using general method
    sample_std_dev = np.std(old_data)
    ci = 1.96 * (sample_std_dev/(math.sqrt(len(old_data))))
    ax.errorbar(1, old_mean_exec_time, yerr=ci, capsize=3, fmt='o', color='red')

    sample_std_dev = np.std(new_data)
    ci = 1.96 * (sample_std_dev/(math.sqrt(len(new_data))))
    ax.errorbar(4, new_mean_exec_time, yerr=ci, capsize=3, fmt='o', color='red')

    #Confidence intervals assuming data is Normal
    sample_std_dev = np.std(old_data, ddof=1)
    ci = 1.96 * (sample_std_dev/(math.sqrt(len(old_data))))
    ax.errorbar(0, old_mean_exec_time, yerr=ci, capsize=3, fmt='o', color='black')

    sample_std_dev = np.std(new_data, ddof=1)
    ci = 1.96 * (sample_std_dev/(math.sqrt(len(new_data))))
    ax.errorbar(3, new_mean_exec_time, yerr=ci, capsize=3, fmt='o', color='black')

    #Confidence intervals using bootstrap method
    bootstrap_ci = bootstrap_CI(new_data, 25, 0.95)
    error = new_mean_exec_time - bootstrap_ci[0]
    ax.errorbar(5, new_mean_exec_time, yerr=error, capsize=3, fmt='o', color='blue')

    bootstrap_ci = bootstrap_CI(old_data, 25, 0.95)
    error = old_mean_exec_time - bootstrap_ci[0]
    ax.errorbar(2, old_mean_exec_time, yerr=error, capsize=3, fmt='o', color='blue')


    plt.ylabel("Mean Execution Time")
    plt.suptitle("Normal Asymptotic and Bootstrap Percentile Confidence Intervals")
    plt.ylim(25,70)
    ax.set_xticks([1,4])
    ax.set_xticklabels(['Old Dataset','New Dataset'])

#Plot of figure 2.10
def fig210():

    #Normal Plot
    fig, ax = plt.subplots(1,2)
    ax[0].plot(joe_data, color='red')
    ax[0].set_xticks(np.arange(0,110,10))
    ax[0].set_yticks(np.arange(-400,500,100))
    ax[0].set_title("Data")
    ax[0].set_xlim(0,100)

    #Autocorrelation Plot
    ax[1].set_title("Autocorrelation")
    ax[1].set_xlim(0,100)
    ax[1].set_xticks(np.arange(0,110,10))
    ax[1].acorr(joe_data ,maxlags=92, color='grey')
    ax[1].axhline(y=1.96/np.sqrt(len(joe_data)), color='blue', linestyle='dotted', xmin=0, xmax=1, linewidth=1)
    ax[1].axhline(y=-1.96/np.sqrt(len(joe_data)), color='blue', linestyle='dotted', xmin=0, xmax=1, linewidth=1)

    #Lag Plots
    fig, axs = plt.subplots(3,3)
    s = pd.Series(joe_data)
    plt.setp(axs, xlim=(-500,500), ylim=(-400,400))

    for i in range(9):
        pd.plotting.lag_plot(s, lag=i+1, ax=axs[int(i/3),i%3], s=1)
        axs[int(i/3),i%3].set(xlabel="", ylabel="", title="h ="+str(i+1))
        
def bootstrap_CI(data, r0, gamma):

    R =  np.ceil((2*r0)/(1-gamma))-1
    bootstrap_means = []

    for i in range(int(R)):
        bootstrap_samples = np.random.choice(data, size=len(data), replace=True)
        bootstrap_mean = np.mean(bootstrap_samples)
        bootstrap_means.append(bootstrap_mean)

    sorted_means = np.sort(bootstrap_means)
    return (sorted_means[r0], sorted_means[(int(R)+1)-r0])

fig210()
plt.show()
