import numpy as np
import pylab as P
from observational_data import *

hpl = 0.6777
Mag0 = -4.61455/0.2587

# Dust Attenuation/Extinction
# only if Dust_Ext == 1
Dust_Ext = 0

# Set of parameters to fit
Obs_Data = [OD2]

# Initial Conditions
L_0in   = 10.0**(18.666666)
M_0in   = 10.0**(11.25)
betain  =  1.2 
gammain =  0.2
MULT    =  1

# Number of Monte-Carlo Steps
MS = 100000

# Monte-Carlo tuning
chi_sqr_treshold = 30
DeltaChi = 0.0001      #
k0       = 0.02        # L_0
k1       = 0.015        # M_0
k2       = 0.02         # beta
k3       = 0.02         # gamma
BlowUp  = 1.0e3       # In case that first or first and second bin is equal to zero
