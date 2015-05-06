__author__ = 'cvogl'

import numpy as np
import matplotlib.pyplot as plt


class Packet:
    def __init__(self):
        self.mu = 0
        self.taur = 10.

    def step(self):
        tau_free = -np.log(np.random.random())
        self.mu = 2 * np.random.random() - 1
        self.taur -= tau_free * self.mu

    def randomwalkpacket(self):
        self.taur = 10.
        self.mu = np.sqrt(np.random.random())
        while self.taur >= 0:
            self.step()
            if self.taur > 10:
                self.randomwalkpacket()
        return self.mu


class Experiment:
    def __init__(self, N):
        self.N = N

    def angular_distribution(self):
        angles = np.zeros(self.N)
        for i in range(self.N):
            Testpacket = Packet()
            angles[i] = Testpacket.randomwalkpacket()
        return angles

    def plot_angular_distribution(self, no_bins):
        angleslist = self.angular_distribution()
        binwidth = 1. / no_bins
        test = [1 - binwidth for i in range(len(angleslist))]
        normvalue = angleslist[angleslist > test].size
        weightslist = [(1. / normvalue) / angleslist[i] for i in range(len(angleslist))]
        bins1 = np.arange(0, 1 + binwidth, binwidth)
        plt.hist(angleslist, bins=bins1, weights=weightslist, facecolor='g', alpha=0.75, histtype='step')
        plt.ylabel('I($\mu$)/I(1)')
        plt.xlabel('$\mu$')

    def plot_theory_angular_distribution(self):
        x = np.linspace(0, 1, num=100)
        Ilist = (0.4 + 0.6 * x)
        plt.plot(x, Ilist, color='r')


Exp1 = Experiment(10 ** 5)
Exp1.plot_angular_distribution(100)
Exp1.plot_theory_angular_distribution()
plt.show()