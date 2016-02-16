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
