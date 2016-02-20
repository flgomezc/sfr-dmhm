import numpy as np
import time
from random             import *
from constants          import *
from settings import *

# 2015-mar-22: Chi2 modification in MCMC

def Luminosity(M,L_0,M_0,beta,gamma):
    """Returns the luminosity of the halo with mass M.

    Instead of use a two parametric function (a power law), we use a
    four-parameter function to reproduce the two slopes in the LF.

    Input parameters:
    M     (double)
    L_0   (double) ~10**17   (Lsun)
    M_0   (double) ~10**11.4 (Msun)
    beta  (double) >0
    gamma (double) > 0"""

    return L_0*M*( (M/M_0)**(-beta) + (M/M_0)**gamma)**(-1)

def StarFormationRate(M,L_0,M_0,beta,gamma):
    """Returns SFR (in Msun yr-1) of a DM halo of mass M

    Input parameters:
    M     (double)
    L_0   (double) ~10**17   (Lsun)
    M_0   (double) ~10**11.4 (Msun)
    beta  (double) >0
    gamma (double) > 0"""

    return Luminosity(M,L_0,M_0,beta,gamma) * 1.4e-28

def Dust_Extinction():
    "Control. Prints if Dust Extinction in constants.py is ON/OFF"
    if ( Dust_Ext == 1):
        print "Dust Extinction ON"
    else:
        print "Dust Extinction OFF"
    #return 0

def initial_positions(nwalkers):
    """Initial position of Random Walkers

    Uses four gaussians to generate random inital parameters."""
    mult= 1.
    p = []
    K0 = k0*mult
    K1 = k1*mult
    K2 = k2*mult
    K3 = k3*mult

    for i in range(nwalkers):
        L_0R   = L_0in  *10**(gauss(0.0,K0))
        M_0R   = M_0in  *10**(gauss(0.0,K1))
        betaR  = betain + gauss(0.0,K2)
        gammaR = gammain+ gauss(0.0,K3)

    ### Some constraints over parameters
        while (L_0R <10**(16.75)) or (L_0R >10**(19.0)):
            L_0R   = L_0in  *10**(gauss(0.0,K0))
        while (M_0R < 10**10.50) or (M_0R > 10**12.00):
            M_0R   = M_0in  *10**(gauss(0.0,K1))
        while (betaR<0) or (betaR>1.6):
            betaR  = betain + gauss(0.0,K2)
        while (gammaR<0) or (gammaR>0.9):
            gammaR = gammain+ gauss(0.0,K3)

        p.append(np.array([L_0R, M_0R, betaR, gammaR]))
    p = np.array(p)
    return p

def ln_likelihood( X, Mass, DataSets ):   #X = [M, L_0, M_0, beta, gamma]
    """ Likelihood function.

    Inputs:
        X = [L_0, M_0, beta, gamma]
        M : Mass Catalog
        DataSets: The set of observations to fit. Example [OD1,OD3]
    """
    L_0   = X[0]
    M_0   = X[1]
    beta  = X[2]
    gamma = X[3]

    ### Restriction over parameters
    if (gamma<0)|(gamma>1.0):
        return -np.inf
    if (beta<0)|(beta>1.0):
        return -np.inf
    if (L_0<0):
        return -np.inf
    if (M_0<0):
        return -np.inf

    ### Create Luminosity Catalog from Halo Mass Catalog and parameters
    L   =   np.zeros(Mass.size)
    L[:]= Luminosity(Mass[:], L_0, M_0, beta, gamma)

    ### Create the Magnitude Catalog with/without dust attenuation
    Mag = 51.82 - 2.5 * np.log10(L)
    if (Dust_Ext == 1):
        Mag[Mag < Mag0] = ( Mag[Mag< Mag0]-4.61455)/1.2587

    ### Create and Normalize the histograms for each data set (DS)
    #   dividing by the bin width and the simulation volume
    HISTO = []
    with np.errstate(divide='ignore'):
        for DS in DataSets:
            aux = 1.0*np.histogram(Mag, bins= DS.bins)[0]
            for i in range(len(aux)):
                aux[i] = np.log10(1.0*aux[i]/
                            ( (DS.bins[i+1] - DS.bins[i] ) * BoxLength**3))
            HISTO.append(aux)
   ### Calcule the likelihood parameter.
    chi_sqr = 0
    for i in range(len(DataSets)):
        for j in range(len(DataSets[i].lf)):
            chi_sqr+= -((DataSets[i].lf[j] - HISTO[i][j])/DataSets[i].err[j]**2)
   ### End of likelihood function.
    return chi_sqr
