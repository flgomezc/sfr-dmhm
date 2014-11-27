import numpy as np
import pylab as P

hpl = 0.6777
Mag0 = -4.61455/0.2587

# Number of Monte-Carlo Steps
MS = 11000

# Monte-Carlo tuning
DeltaChi = 0.2
K0 = 0.02        # L_0
K1 = 0.02        # M_0
K2 = 0.02        # beta 
K3 = 0.02        # gamma

# Dust Attenuation/Extinction
# only if Dust_Ext == 1
Dust_Ext = 1

L_0Panic    = 10.0**(17.9)
M_0Panic    = 10.0**(11.2)
betaPanic  =  0.7
gammaPanic =  0.1
    
