import numpy as np
import matplotlib.pyplot as plt

class dataset():
    def __init__(self, name, filename, PathToObs):
        self.name = name
        self.raw = np.loadtxt(PathToObs + filename)

        l = len(self.raw)

        bins = []
        for i in range(l):
            bins.append(self.raw[i,0])
        bins.append(self.raw[-1,1])
        self.bins = np.array(bins)

        mag = ( self.raw[:,0] + self.raw[:,1] )/2.0
        self.mag = np.array(mag)

        self.lum = self.raw[:,2]

        self.err = self.raw[:,3]

    def scatter(self):
        plt.scatter(self.mag, self.lum)
