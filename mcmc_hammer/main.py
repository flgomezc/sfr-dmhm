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
