import numpy as np
from matplotlib import  pyplot as plt
# %matplotlib inline

plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.figsize'] = 20, 7
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 14


def plot_runtimes(kind):
    if kind == 'naive':
        x = np.arange(1, 6, dtype='int')
        y = np.load("data/naive_runs.npy")
        plt.loglog(x, y)
    elif kind == "counter":
        x = np.arange(1, 6, dtype='int')
        y = np.load("data/counter_runs.npy")
        plt.loglog(x, y)
    elif kind == "both":
        f, ax = plt.subplots()
        x = np.arange(1, 6, dtype='int')
        y = np.load("data/naive_runs.npy")
        ax.loglog(x, y, label="Naive")
        y = np.load("data/counter_runs.npy")
        ax.loglog(x, y, label='Counter')
        ax.legend()

    plt.show()