# Task 1
# Produce results as in Figs. 6.5, 6.7 and 6.10

import math as math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf

m = 2 ** 31 - 1  # modulus
a = 16807  # multiplier
n = 1000


# Implementation of a linear congruence generator
def lcg(seed):
    while True:
        seed = ((a * seed) % m)
        xn = seed / m
        yield xn


# ------ Figure 6.5 start ------

# Generate n variables from the generator initialized with seed = 1
generator = lcg(1)
gen1 = [next(generator) for _ in range(n)]
print(gen1)

# Plot grid of 1x3 dimension
fig = plt.figure(figsize=(7, 15))
subfields = fig.subfigures(3, 1)
bottom = subfields[2].subplots(3, 3)

# Lag plot
s = pd.Series(gen1)
for i in range(9):
    pd.plotting.lag_plot(s, lag=i + 1, ax=bottom[int(i / 3), i % 3], s=1)
    bottom[int(i / 3), i % 3].set(xlabel="", ylabel="", title="h =" + str(((i + 1) * 100)))

subfields[2].subplots_adjust(hspace=0.4, wspace=0.3)
bottom[2, 1].set_xlabel("(c)")

# Auto-correlation plot
center = subfields[1].subplots(1, 1)
plot_acf(gen1, lags=30, zero=False, markersize=3, linewidth=1, ax=center)
center.set_xlabel("(b)")
center.set_xlim(0, 31)
center.set_ylim(-0.2, 1.2)

# QQplot
gen1.sort()
atop = subfields[0].subplots(1, 1)
atop.set_title("uniform QQPlot")
atop.set_xlabel("(a)")
atop.set_xlim(0, 1000)
atop.set_ylim(0, 1)
atop.scatter(np.arange(1000), gen1, s=0.2)
plt.savefig("img/Figure 65.png", bbox_inches='tight')
plt.show()

# ------ Figure 6.5 end ------

# ------ Figure 6.6 start ------

# Initiate 3 different generators
var = 1000
gen1 = lcg(1)  # seed = 1
gen2 = lcg(2)  # seed = 2
x1 = [next(gen1) for _ in range(var)]
x2 = [next(gen2) for _ in range(var)]

gen3 = lcg(x1[-1])  # seed = last variable generated of lcg(1) sequence
x3 = [next(gen3) for _ in range(var)]

fig, ax = plt.subplots(2, 1, figsize=(7, 12))
ax[0].scatter(x1, x2, s=1)
ax[0].set(title='Two streams, seed = 1 and 2',
          xlim=(0, 1),
          ylim=(0, 1),
          xticks=(np.arange(0, 1.1, 0.1)),
          yticks=(np.arange(0, 1.1, 0.1)))

ax[1].scatter(x1, x3, s=1)
ax[1].set(title='Two Streams, seeds = 1 and 6.628930e−001',
          xlim=(0, 1),
          ylim=(0, 1),
          xticks=(np.arange(0, 1.1, 0.1)),
          yticks=(np.arange(0, 1.1, 0.1)))
plt.savefig("img/Figure 67.png", bbox_inches='tight')


# ------ Figure 6.6 end ------
# ------ Figure 6.10 start ------
def f(x):
    return ((math.sin(x)) / x) ** 2


def sampling_610a():
    while True:
        x = np.random.uniform(-10, 10)
        u = np.random.uniform(0, 1)
        if u <= f(x):
            return x


def sampling_610b():
    while True:
        x_1 = np.random.uniform(0, 1)
        x_2 = np.random.uniform(0, 1)
        u = np.random.uniform(0, 1)
        if u <= abs(x_1 - x_2):
            return x_1, x_2


f_x = [sampling_610a() for _ in range(2000)]
fx1_b = []
fx2_b = []
for _ in range(2000):
    x_1, x_2 = sampling_610b()
    fx1_b.append(x_1)
    fx2_b.append(x_2)

fnp = np.array(f_x)
figs, ax = plt.subplots(2, 1, figsize=(5, 10))
ax[0].hist(fnp, bins=np.arange(-10, 10, 0.1))
ax[0].set(xlim=(-10, 10),
          ylim=(0, 90),
          xlabel="(a)",
          xticks=(np.arange(-10, 12, 2)))

ax[1].scatter(fx1_b, fx2_b, s=1)
ax[1].set(xlim=(0, 1),
          ylim=(0, 1),
          xticks=(np.arange(0, 1.1, 0.1)),
          yticks=(np.arange(0, 1.1, 0.1)),
          xlabel="(b)")
plt.savefig("img/Figure 610.png", bbox_inches='tight')
# ------ Figure 6.10 end ------

plt.show()
