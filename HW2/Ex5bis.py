# LCG 1
a1 = 18
m1 = 101
x1 = 1
samples1 = []
for i in range(1000):
    x1 = (a1 * x1) % m1
    samples1.append(x1)

# LCG 2
a2 = 2
m2 = 101
x2 = 1
samples2 = []
for i in range(1000):
    x2 = (a2 * x2) % m2
    samples2.append(x2)

samples1.sort()
samples2.sort()

print(samples2)
print(samples1)

import matplotlib.pyplot as plt

# LCG 1
plt.scatter(samples1[:-1], samples1[1:], s=10)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title("LCG 1")
plt.show()

# LCG 2
plt.scatter(samples2[:-1], samples2[1:], s=10)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title("LCG 2")
plt.show()
