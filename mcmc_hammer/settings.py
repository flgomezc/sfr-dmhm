import numpy as np
import matplotlib.pyplot as plt

from observations import *
from constants import *

######################################################################
# Observational Datasets
######################################################################
PathToObs = "../data/obs/"

OBS0 = dataset("Bouwens", "Bouwens_2015.dat", PathToObs)
OBS1 = dataset("Finkelstein","Finkelstein_2015.dat", PathToObs)
OBS2 = dataset("Willott","Willott_2013.dat", PathToObs)

######################################################################
# Catalog and Attenuation options
######################################################################
Dust_Ext = 1             # Dust Attenuation/Extinction ON(1) / OFF(0)
NB = range(0,1)          # Range with the number of catalogs to work
BoxLength = 250.0 /hpl   # Box Size in Mpc. Must be divided by the
                         # Hubble parameter in the 2013 Planck cosmology.
Obs_Data = [OBS1]         # Set of parameters to fit

######################################################################
# MCMC options
######################################################################
MS = 100-1           # Number of Monte-Carlo Steps

L_0in   = 10.0**(18.0) # initial parameters set
M_0in   = 10.0**(11.25)
betain  =  0.75
gammain =  0.4

chi_sqr_treshold = 30  # Monte-Carlo tuning
DeltaChi = 0.0001      #
k0       = 0.02        # L_0
k1       = 0.015       # M_0
k2       = 0.02        # beta
k3       = 0.02        # gamma
BlowUp  = 1.0e3        # In case that first and/or second bin are equal to zero

######################################################################
# Output files
######################################################################
if (Dust_Ext ==1):
    MCMC_reg = [open( 'results_w_ext_/%i.dat' %filenumber, 'w')
    for filenumber in NB]
else:
    MCMC_reg = [open( 'results_wo_ext_/%i.dat' %filenumber, 'w')
    for filenumber in NB]
