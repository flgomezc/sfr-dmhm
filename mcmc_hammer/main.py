import numpy as np
import matplotlib.pyplot as plt
import emcee
from random import *

from constants import *
from observations import *
from settings import *

import functions

### Load halo mass catalog and divide by the Hubble parameter
M = np.loadtxt(PathToCat+str(BN)+".dat", usecols=(3,), skiprows=0) / hpl
print len(M)

### MCMC settings
DataSets=[OBS1]
ndim     = 4
nwalkers = 8*2
nstepsburn=10
nstepsrun = 10
#Initial set of positions for the walkers
p0 = functions.initial_positions(nwalkers) #(initial guess)

# Initialize the sampler with the chosen specs.
# threads==number of processors
sampler = emcee.EnsembleSampler(nwalkers, ndim, functions.ln_likelihood,
                                args=[M, DataSets],threads=4)

pos, prob, state = sampler.run_mcmc(p0, nstepsburn)
print pos
print prob
print state
