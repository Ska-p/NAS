import math
import time
from random import random

import matplotlib.pyplot as plt
import numpy as np


def binomial_from_cdf_inversion(n, p):
    u = random()
    c = p / (1 - p)
    i = 0
    f = pr = pow((1 - p), n)
    while True:
        if u < f:
            return i
        pr = ((c * (n - i)) / (i + 1)) * pr
        f += pr
        i += 1


def bernoulli(p):
    return int(np.random.uniform(0, 1) <= p)


def binomial_from_bernoulli(n, p):
    x = 0
    for _ in range(n):
        x += bernoulli(p)
    return x


def binomial_from_geometric(n, p):
    count = 0
    sum = 0
    while sum < n:
        x = generate_geometric(p)
        sum += x
        count += 1
    return count


def generate_geometric(p):
    # Generate a geometric random variable with probability p
    x = np.floor((math.log(random()) / math.log(1 - p)))
    return int(x)


n_var = np.arange(4, 24, 4)
prob = 0.1
fig, ax = plt.subplots(3, 1, figsize=(7, 15))
for n_vars in n_var:
    cdf = []
    ber = []
    geo = []
    prob = 0.1
    while prob < 0.9:
        start = time.time()
        for i in range(10000):
            binomial_from_cdf_inversion(n_vars, prob)
        end = time.time()
        cdf.append(end - start)

        start = time.time()
        for i in range(10000):
            binomial_from_bernoulli(n_vars, prob)
        end = time.time()
        ber.append(end - start)

        start = time.time()
        for i in range(10000):
            binomial_from_geometric(n_vars, prob)
        end = time.time()
        geo.append(end - start)
        prob += 0.1
    ax[0].plot(np.arange(0.1, 1, 0.1), cdf, label=n_vars)
    ax[1].plot(np.arange(0.1, 1, 0.1), ber, label=n_vars)
    ax[2].plot(np.arange(0.1, 1, 0.1), geo, label=n_vars)

ax[0].set(title="CDF Inversion",
          ylabel="Time [s]",
          xlabel="Probability of success",
          xlim=(0.1, 0.9),
          ylim=(0, max(cdf)+np.average(cdf))
          )
ax[1].set(title="Sequence of n Bernoulli variables",
          ylabel="Time [s]",
          xlabel="Probability of success",
          xlim=(0.1, 0.9),
          ylim=(0, max(ber)+min(ber))
          )
ax[2].set(title="Geometric string of zeroes",
          ylabel="Time [s]",
          xlabel="Probability of success",
          xlim=(0.1, 0.9),
          ylim=(0, max(geo)+min(geo))
          )

plt.subplots_adjust(hspace=0.2)
plt.savefig("img/Exercise2.png", bbox_inches='tight')
plt.show()
print("END")
