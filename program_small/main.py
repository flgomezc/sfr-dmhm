from random import *
from observational_data import *
from constants import *
from functions import *
import numpy as np

# Number of boxes
NB = range(0,1)

# Box Size in Mpc. Must be divided by the hubble parameter in
# the 2013 Planck cosmology. (hpl defined in "constants.py")
BoxLength = 125.0 / hpl

if (Dust_Ext ==1):
    MCMC_reg = [open( 'results_w_ext_/%i.dat' %filenumber, 'w') for filenumber in NB]
else:
    MCMC_reg = [open( 'results_wo_ext_/%i.dat' %filenumber, 'w') for filenumber in NB]
Dust_Extinction()

i = 0
for DATA in NB:
    STR = '../data/P_Bolshoi/cells/'+str(DATA)+'.dat'
    M = np.loadtxt(STR,usecols=(3,), skiprows=0)
########## Halo mass must be divided by the Hubble Parameter ###
    M = M/hpl                                                  #
################################################################

    # Initial conditions and dataset are in constants.py
    MCMC( BoxLength, MS, M, L_0in, M_0in, betain, gammain, MCMC_reg[i],*Obs_Data)
    i+=1
    print DATA
