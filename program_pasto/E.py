from random import *
from observational_data import *
from constants import *
from functions import *
import numpy as np

# Number of boxes
NB = range(32,40)

# Box Size in Mpc. Must be divided by the hubble parameter in 
# the 2013 Planck cosmology. (hpl defined in "constants.py")
BoxLength = 250.0 / hpl

if (Dust_Ext ==1):
    MCMC_reg = [open( 'results_w_ext/%i.dat' %filenumber, 'w') for filenumber in NB]
else:
    MCMC_reg = [open( 'results_wo_ext/%i.dat' %filenumber, 'w') for filenumber in NB]
Dust_Extinction()
i = 0

for DATA in NB:
    STR = '../data/MD_3840_Planck1/BDM/Small_Cells/'+str(DATA)+'.dat'
    M = np.loadtxt(STR,usecols=(3,), skiprows=0)
########## Halo mass must be divided by the Hubble Parameter ###
    M = M/hpl                                                  #
################################################################
    L_0   = 10.0**(17.94)
    M_0   = 10.0**(11.25)
    beta  =  0.8
    gamma =  0.1424

    Obs_Data = [OD1]
    
    MCMC( BoxLength, MS, M, L_0, M_0, beta, gamma,MCMC_reg[i],*Obs_Data)
    i+=1
    print DATA
