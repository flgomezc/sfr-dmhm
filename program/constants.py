import numpy as np
import pylab as P

hpl = 0.6777
Mag0 = -4.61455/0.2587

# Dust Attenuation/Extinction
# only if Dust_Ext == 1
Dust_Ext = 0

# Number of Monte-Carlo Steps
MS = 11000

# Monte-Carlo tuning
DeltaChi = 1.0
K0 = 0.01        # L_0
K1 = 0.01        # M_0
K2 = 0.01        # beta
K3 = 0.01        # gamma

# This part of the code breaks
# the glass in case of emergency
# returning to good parameters

L_0Panic    = 10.0**(17.9)
M_0Panic    = 10.0**(11.2)
betaPanic  =  0.5
gammaPanic =  0.2

if Dust_Ext == 1:
    L_0Panic    = 10.0**(18.05)
    M_0Panic    = 10.0**(11.10)
    betaPanic   =  0.2
    gammaPanic  =  0.30
