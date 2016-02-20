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

        p.append(array([L_0R, M_0R, betaR, gammaR]))
    return p



def lnprob( X, Mass, DataSets ):   #X = [M, L_0, M_0, beta, gamma]
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

    #print "beta= ", beta, ", gamma= ", gamma
    ### Restriction over parameters
    if (gamma<0)|(gamma>1.0):
        return -numpy.inf
    if (beta<0)|(beta>1.0):
        return -numpy.inf
    if (L_0<0):
        return -numpy.inf
    if (M_0<0):
        return -numpy.inf





def MCMC( BoxLength, MonteCarloSteps, M, L_0, M_0, beta, gamma,MCMC_reg, *DataSets):
    """
Markov Chain Monte Carlo function.

This function writes MonteCarloSteps lines in the input file MCMC_reg.
The jump-size on the parameters space is controlled by the "constants.py" file

Arguments:
        Box size (double)
        Monte-Carlo Steps (int)
        Mass (array)
        4 parameters(double)
        Output filename (string)
        DataSets (list) This list contains the names of the observational data
        to be fitted.
     """
    seed(None)
    L   = np.zeros(M.size)
    L_R = np.zeros(M.size)
    L[:] = Luminosity( M[:], L_0, M_0, beta, gamma)
    Magnitude_UV_galaxy_list = 51.82 - 2.5 * np.log10(L[:])

    ### Dust Extinction
    if (Dust_Ext == 1):
        Mag = Magnitude_UV_galaxy_list
        Mag[Mag< Mag0] = ( Mag[Mag< Mag0]-4.61455)/1.2587
        Magnitude_UV_galaxy_list_R = Mag

    ### Create histograms & Normalize the histograms
########################################################### Here is the problem
    HISTO = []

    for DS in DataSets:
# ---> Work here
        HISTO.append(aux)

    ### Calcule Chi Square using number of Degrees of Freedom
    NOB = 0
    chi_sqr = 0.0

# ---> Work here
    chi_sqr /= (NOB-4)

    MCMC_reg.write('#'+str(time.strftime("%Y-%m-%d  %H:%M")) + '\n')
    MCMC_reg.write('# k:\t'+str(k0)+'\t'+str(k1)+'\t'+str(k2)+'\t'+str(k3)+'\n')
    MCMC_reg.write('# k Multiplier = '+str(MULT)+'\n')
    MCMC_reg.write('# DataSets ='+str(Obs_Data[:][0][3])+'\n')

    MCMC_reg.write("# L_0 \t M_0 \t beta \t gamma \t chi_sqr \t Number of Bins\n")
    MCMC_reg.write(str(log10(L_0))+"\t"+
                   str(log10(M_0))+"\t"+
                   str(beta)      +"\t"+
                   str(gamma)     +"\t"+
                   str(chi_sqr)   +"\t"+
                   str(NOB)       +"\n")

    best_chi   = chi_sqr
    best_L_0   = L_0
    best_M_0   = M_0
    best_beta  = beta
    best_gamma = gamma

    ###################################
    # Markov Chain Monte Carlo Starts #
    ###################################


    # First of all, the histogram with the original parameters must be calculated,
    # included the Xi_square deviation
    for COUNTER in range(MonteCarloSteps):
      print COUNTER
        # Then the parameters are changed in order to calculate the new histogram

        ### Some constraints over parameters

        #for i in range(M.size):

        ### Dust Extinction

        ### Create histograms & Normalize the histograms

        ### Calcule Chi Square using number of Degrees of Freedom

        ### Flags

    MCMC_reg.close()

        ### Normalization
