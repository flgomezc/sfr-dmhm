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
# Box Size in Mpc/ hpl; the Hubble parameter using the 2013 Planck cosmology.
######################################################################
Obs_Data = [OBS1]        # Set of parameters to fit
Dust_Ext = 1             # Dust Attenuation model ON(1) / OFF(0)
Catalog = "Planck"       # Options: Bolshoi or Planck
BN = 0                   # Box Number

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
# Create multiple output files
######################################################################
if (Dust_Ext ==1):
    filename = 'mcmc_steps/dust_on/'+str(BN)+'.dat'
#    MCMC_reg = open( filename, 'w')
else:
    filename = 'mcmc_steps/dust_off/'+str(BN)+'.dat'
MCMC_reg = open( filename, 'w')
# MCMC_reg = [open( 'results_wo_ext_/%i.dat' %filenumber, 'w')
# for filenumber in NB]


if Catalog == "Bolshoi":
  BoxLength = 250.0 / hpl
  PathToCat = "../data/theory/BolshoiP_2048_z6_Mhalo/L_125_Mpc_cells/"
  if BN >= 64:
    exit("settings.py error:\n\tWrong Box Number\n\t0<=BN<8 for Bolshoi sim.")
elif Catalog == "Planck":
  BoxLength = 250.0 /hpl
  PathToCat = "../data/theory/MD_3840_Plank1_z6_Mhalo/L_250_Mpc_cells/"
  if BN >= 64:
    exit("settings.py error:\n\tWrong Box Number\n\t0<=BN<64 for Planck sim.")
else:
  err_msg = str("settings.py error: \n\tmissmatching catalog name\n\t Please"+
  "choose one properly between \"Bolshoi\" and \"Planck\"\n" )
  exit(err_msg)
