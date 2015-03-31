import numpy as np
import pylab as P
import time
from random             import *
from constants          import *
from observational_data import *

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
Markov Chain  Monte Carlo function.

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
    HISTO = []

    for DS in DataSets:
        aux = 1.0 * np.histogram(Magnitude_UV_galaxy_list, bins= array(DS[1]) )[0]
        for i in range(len(aux)):
            aux[i] = aux[i]/( (DS[1][i+1] - DS[1][i] ) * BoxLength**3)
        HISTO.append(aux)

    ### Calcule Chi Square using number of Degrees of Freedom
    NOB = 0
    chi_sqr = 0.0
    for i in range(len(HISTO)):
        if (HISTO[i][0]==0):
            HISTO[i][0]+= HISTO[i][1]/1000.0

        for j in range(HISTO[i].size):
            if( HISTO[i][j] != 0.0 ):
                chi_sqr = chi_sqr + 0.5*( log10(HISTO[i][j]/DataSets[i][0][1][j]) / DataSets[i][2][j])**2
                NOB = NOB + 1
            else:
                NOB += DeltaChi
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
        # Then the parameters are changed in order to calculate the new histogram

        K0 = k0
        K1 = k1
        K2 = k2
        K3 = k3


        L_0R   = L_0  *10**(gauss(0.0,K0))
        M_0R   = M_0  *10**(gauss(0.0,K1))
        betaR  = beta + gauss(0.0,K2)
        gammaR = gamma+ gauss(0.0,K3)

        p = random.rand()


        ### Some constraints over parameters
        while (L_0R <10**(16.75)) or (L_0R >10**(19.0)):
            L_0R   = L_0  *10**(gauss(0.0,K0))
        while (M_0R < 10**10.50):
            M_0R   = M_0  *10**(abs(gauss(0.0,K1)))
            print "new M_0R", M_0R
        while (betaR<0) or (betaR>1.5):
            betaR  = beta + gauss(0.0,K2)
        while (gammaR<0) or (gammaR>0.6):
            gammaR = gamma+ gauss(0.0,K3)

        #for i in range(M.size):
        L_R[:]    = Luminosity( M[:], L_0R, M_0R, betaR, gammaR)
        Magnitude_UV_galaxy_list_R = 51.82 - 2.5 * log10(L_R[:])

        ### Dust Extinction
        if (Dust_Ext == 1):
            Mag = Magnitude_UV_galaxy_list_R
            Mag[Mag< Mag0] = ( Mag[Mag< Mag0]-4.61455)/1.2587
            Magnitude_UV_galaxy_list_R = Mag

        ### Create histograms & Normalize the histograms
        HISTO_R = []
        for DS in DataSets:
            aux = 1.0 * np.histogram(Magnitude_UV_galaxy_list_R, bins= DS[1] )[0]
            for i in range(len(aux)):
                aux[i] = aux[i]/( (DS[1][i+1] - DS[1][i] ) * BoxLength**3)
            HISTO_R.append(aux)

        ### Calcule Chi Square using number of Degrees of Freedom
        NOB = 0
        nob = 0
        chi_sqr_R = 0.0
        FLAG = "   "
        for i in range(len(HISTO_R)):
            if (HISTO_R[i][2]==0):
                HISTO_R[i][2]+= HISTO_R[i][3]/BlowUp
                FLAG +="+3 "
                nob -= 1
            if (HISTO_R[i][1]==0):
                HISTO_R[i][1]+= HISTO_R[i][2]/BlowUp
                FLAG +="+2 "
                nob -= 1
            if (HISTO_R[i][0]==0):
                HISTO_R[i][0]+= HISTO_R[i][1]/BlowUp
                FLAG +="+1 "
                nob -= 1
            if (HISTO_R[i][-1]<HISTO_R[i][-2]):
                FLAG += 'Tail is going down!'
                print   'Tail is going down!'

            for j in range(HISTO_R[i].size):
                if( HISTO_R[i][j] != 0.0 ):
                    chi_sqr_R = chi_sqr_R + 0.5*( log10( HISTO_R[i][j]/DataSets[i][0][1][j] ) / DataSets[i][2][j] )**2
                    NOB = NOB + 1.0
                    nob = nob + 1
                else:
                    NOB += DeltaChi                                           ###  2015-03-22
#                        chi_sqr_R = chi_sqr_R + DeltaChi                     ###  2015-03-22
                    FLAG += " #"

        chi_sqr_R /= (NOB-4.0) ### Number of Degrees of Freedom = Number Of Bins-4 parameters

#   If chi_squ grows without limit, then return to the best parameters

        if (chi_sqr_R >= 0):
        # If the new chi2 is better, then the new set of parameters is accepted
            Delta_chi = chi_sqr_R - chi_sqr
            if ( Delta_chi < 0):
                L_0    = L_0R
                M_0    = M_0R
                beta   = betaR
                gamma  = gammaR
                HISTO  = HISTO_R
                chi_sqr= chi_sqr_R
            else:
                if ( p < exp( -Delta_chi) ): ## 2015-mar-24
                    L_0    = L_0R
                    M_0    = M_0R
                    beta   = betaR
                    gamma  = gammaR
                    HISTO  = HISTO_R
                    chi_sqr= chi_sqr_R
                    FLAG += "*"
        else:
            print "# WARNING: Chi2 < 0 at step #",COUNTER
            L_0   = L_0in
            M_0   = M_0in
            beta  = betain
            gamma = gammain
            chi_sqr_R = 2
            FLAG += " Chi2 <0!!! Returning to initial parameters"


        # Storing all the good points.
        # L_0, M_0, beta, gamma, chi_sqr, numberofbins, flag
        MCMC_reg.write(
                            str(log10(L_0))+"\t"+
                            str(log10(M_0))+"\t"+
                            str(beta)      +"\t"+
                            str(gamma)     +"\t"+
                            str(chi_sqr)   +"\t"+
                            str(nob)       +"\t"+
                            str(FLAG)      +"\n")
    # End of the loop

    MCMC_reg.close()

def SingleHistogram( BoxLength, BOX, L_0, M_0, beta, gamma, DataSets):
    """
Single Histogram Function.

This function returns the histogram for a single box in the catalog.


Arguments:
    Box size       (double)
    Mass           (array)
    4 parameters   (double) L_0, M_0, beta, gamma
    DataSets       (list) This list contains the names of the observational data
                     to be fitted. E.j.
    """
    STR = '../data/MD_3840_Planck1/BDM/Small_Cells/'+str(BOX)+'.dat'

    M = np.loadtxt(STR,usecols=(3,), skiprows=0)
########## Halo mass must be divided by the Hubble Parameter
    M = (1.0*M)/hpl

    L   = np.zeros(M.size)
    L_R = np.zeros(M.size)
    L[:] = Luminosity( M[:], L_0, M_0, beta, gamma)
    Magnitude_UV_galaxy_list = 51.82 - 2.5 * np.log10(L[:])

    ### Dust Extinction
    if (Dust_Ext == 1):
        Mag = Magnitude_UV_galaxy_list
        Mag[Mag< Mag0] = ( Mag[Mag< Mag0]-4.61455 )/1.2587
        Magnitude_UV_galaxy_list = Mag

    ### Create Histogram list
    HISTO = []

    for k in range(len(DataSets)):
        ### Galaxy counting
        aux = 1.0 * np.histogram(Magnitude_UV_galaxy_list, bins= DataSets[k][1] )[0]
        ### Normalization
        for i in range(len(aux)):
            aux[i] = aux[i]/( (DataSets[k][1][i+1] - DataSets[k][1][i] ) * BoxLength**3)
        HISTO.append(aux)
    print HISTO

    NOB = 0
    chi_sqr = 0.0

    for i in range(len(HISTO)):
        if (HISTO[i][0]==0):
            HISTO[i][0]+= HISTO[i][1]/1000.0

        for j in range(HISTO[i].size):
            if( HISTO[i][j] != 0.0 ):
                chi_sqr = chi_sqr + 0.5*( log10( HISTO[i][j]/DataSets[i][0][1][j] ) / DataSets[i][2][j])**2
                NOB = NOB + 1
            else:
                NOB += DeltaChi
    chi_sqr /= (NOB-4)
    print 'Chi2 =', chi_sqr
    return HISTO


def FullHistograms():
    histo0 = []
    if ( Dust_Ext ==1):
        parameters = np.loadtxt('analysis/best_parameters_w_ext.dat',usecols=(0,1,2,3), skiprows=0);
    else:
        parameters = np.loadtxt('analysis/best_parameters_wo_ext.dat',usecols=(0,1,2,3), skiprows=0);

    L_0   = 10**parameters[:,0]
    M_0   = 10**parameters[:,1]
    beta  = parameters[:,2]
    gamma = parameters[:,3]
    for k in range(64):
        histo0.append( SingleHistogram( 250/hpl, k, L_0[k], M_0[k], beta[k], gamma[k]) )

    Dust_Extinction()

    return   histo0
