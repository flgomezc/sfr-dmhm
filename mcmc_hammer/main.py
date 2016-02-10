import numpy as np
import emcee
from random import *

from obs_dat import *
from constants import *
from functions import *

Dust_Extinction()

i = 0
for DATA in NB:
    STR = '../data/MD_3840_Planck1/BDM/Small_Cells/'+str(DATA)+'.dat'
    M = np.loadtxt(STR,usecols=(3,), skiprows=0)
########## Halo mass must be divided by the Hubble Parameter ###
    M = M/hpl                                                  #
################################################################

    # Initial conditions and dataset are in constants.py
    MCMC( BoxLength, MS, M, L_0in, M_0in, betain, gammain, MCMC_reg[i],*Obs_Data)
    i+=1
    print DATA
