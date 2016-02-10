import numpy as np
from obs_dat import *

######################################################################
# Constants
######################################################################
hpl = 0.6777             # Hubble parameter in 2013 Planck Cosmology.
Mag0 = -4.61455/0.2587   # Limit magnitude

######################################################################
# Catalog and Attenuation options
######################################################################
Dust_Ext = 1             # Dust Attenuation/Extinction ON(1) / OFF(0)
NB = range(0,1)          # The number of catalogs to work
BoxLength = 250.0 /hpl   # Box Size in Mpc. Must be divided by the 
                         # Hubble parameter in the 2013 Planck cosmology. 
Obs_Data = [OD1]         # Set of parameters to fit

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
BlowUp  = 1.0e3        # In case that first or first and second bin is equal to zero


######################################################################
# Output files
######################################################################
if (Dust_Ext ==1):
    MCMC_reg = [open( 'results_w_ext_/%i.dat' %filenumber, 'w') for filenumber in NB]
else:
    MCMC_reg = [open( 'results_wo_ext_/%i.dat' %filenumber, 'w') for filenumber in NB]

