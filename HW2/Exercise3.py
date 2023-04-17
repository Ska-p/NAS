import time
from random import random

import matplotlib.pyplot as plt
import numpy as np


def poisson_from_cdf(lam):
    u = random()
    i = 0
    f = p = np.exp(-lam)
    while u >= f:
        p = (lam * p) / (i + 1)
        f += p
        i += 1
    return i


def poisson_from_sum(lam):
    i = 0
    s = 0
    while s <= 1:
        s += np.random.exponential(1 / lam)
        i += 1
    return i - 1


def poisson_from_product(lam):
    i = 0
    prod = 1
    while prod > np.exp(-lam):
        prod *= np.random.uniform(0, 1)
        i += 1
    return i - 1


cdf = []
sums = []
prod = []
lam_val = np.arange(20, 220, 20)

for val in lam_val:
    start = time.time()
    for i in range(10000):
        poisson_from_cdf(val)
    end = time.time()
    cdf.append(end - start)

    start = time.time()
    for i in range(10000):
        poisson_from_sum(val)
    end = time.time()
    sums.append(end - start)

    start = time.time()
    for i in range(10000):
        poisson_from_product(val)
    end = time.time()
    prod.append(end - start)

fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.plot(lam_val, cdf, label="CDF")
ax.plot(lam_val, sums, label="Sum")
ax.plot(lam_val, prod, label="Product")
ax.legend()
ax.set_xlim(min(lam_val), max(lam_val))
ax.set_xticks(lam_val)
ax.set_ylabel("Time [s]")
ax.set_xlabel("Lambda")
plt.savefig("img/Exercise3.png", bbox_inches='tight')
plt.show()

print("END")
