import numpy as np
import pylab as P
from observational_data import *

hpl = 0.6777
Mag0 = -4.61455/0.2587

# Dust Attenuation/Extinction
# only if Dust_Ext == 1
Dust_Ext = 1

# Set of parameters to fit
Obs_Data = [OD1]

# Initial Conditions
L_0in   = 10.0**(17.94)
M_0in   = 10.0**(11.25)
betain  =  0.8
gammain =  0.1424

# Number of Monte-Carlo Steps
MS = 20000-2

# Monte-Carlo tuning
chi_sqr_treshold = 30
DeltaChi = 0.0001      #
k0       = 0.01        # L_0
k1       = 0.01       # M_0
k2       = 0.001       # beta
k3       = 0.001       # gamma
MULT      = 10
BlowUp  = 1.0e20       # In case that first or first and second bin is equal to zero



# This part of the code breaks
# the glass in case of emergency
# returning to good parameters
#L_0Panic    = 10.0**(17.9)
#M_0Panic    = 10.0**(11.2)
#betaPanic  =  0.5
#gammaPanic =  0.2
#
#if Dust_Ext == 1:
#    L_0Panic    = 10.0**(18.05)
#    M_0Panic    = 10.0**(11.10)
#    betaPanic   =  0.2
#    gammaPanic  =  0.30
