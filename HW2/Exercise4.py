import matplotlib.pyplot as plt
import numpy as np


def lcg(seed, a, m):
    while True:
        seed = (a * seed) % m
        xn = seed / m
        yield xn


def plot_pairs(rand_nums, title):
    pairs = [(rand_nums[i], rand_nums[i + 1]) for i in range(len(rand_nums) - 1)]

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.scatter(*zip(*pairs), s=5)
    ax.set(xlim=(0, 1),
           ylim=(0, 1))
    plt.title(title)
    # strt = "img/Ex" + str(np.random.uniform()) + ".png"
    # plt.savefig(strt, bbox_inches='tight')
    plt.show()


def plot_triples(rand_nums):
    triples = [(rand_nums[i], rand_nums[i + 1], rand_nums[i + 2]) for i in range(len(rand_nums) - 2)]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(*zip(*triples), s=5)
    ax.set(xlim=(0, 1),
           ylim=(0, 1),
           zlim=(0, 1))
    ax.view_init(elev=30, azim=60)
    # plt.savefig("img/Ex5b.png", bbox_inches='tight')
    plt.show()


# ------ Exercise 4 ------
generator = lcg(1, 18, 101)
lcg_1 = [next(generator) for _ in range(1000)]
lcg1 = np.array(lcg_1)
print(lcg1)
plot_pairs(lcg1, "lcg1")

generator = lcg(1, 2, 101)
lcg2 = [next(generator) for _ in range(1000)]
plot_pairs(lcg2, "lcg2")
l2 = np.array(lcg2)
print(l2)
for x in range(1, len(lcg2)):
    if lcg2[0] == lcg2[x]:
        print(x)
        break

for x in range(1, len(lcg1)):
    if lcg1[0] == lcg1[x]:
        print(x)
        break

# ------ Exercise 5 ------
generator = lcg(1, 65539, 2 ** 31)
lcg3 = [next(generator) for _ in range(1000)]
plot_pairs(lcg3, "lcg3")
plot_triples(lcg3)
plt.show()
