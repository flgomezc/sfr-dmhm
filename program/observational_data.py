# Last modification: 2014-nov-26 - Bogota
# New lists created

from numpy import *

HIST1_bins=[-22.75,-22.25,-21.75,-21.25,-20.75,-20.25]
Willott = array(
[# Mag,LumFunct, low_err, upp_err #
[-22.5, 2.66E-8, 9.08E-9, 7.78E-8],
[-22.0, 2.18E-6, 8.70E-7, 9.70E-6],
[-21.5, 1.45E-5, 2.88E-6, 2.92E-5],
[-21.0, 1.29E-4, 7.06E-5, 2.19E-4],
[-20.5, 2.30E-4, 9.34E-5, 5.77E-4]
])
Obs_data1 = zeros([5,4])
Obs_data1_log10 = zeros([5,4])
Obs_data1yerror = [array(Willott[:,1]-Willott[:,2]),array(Willott[:,3]-Willott[:,1])]
for i in range(5):
    Obs_data1[i,0]=Willott[i,0]
    Obs_data1[i,1]=Willott[i,1]
    Obs_data1[i,2]=0
    Obs_data1[i,3]=0.25
    Obs_data1_log10[i,0]=Willott[i,0]
    Obs_data1_log10[i,1]=log10(Willott[i,1])
    Obs_data1_log10[i,2]=0
    Obs_data1_log10[i,3]=0.25
Obs_data1_log10yerror = [array(log10(Willott[:,1]/Willott[:,2])),array(log10(Willott[:,3]/Willott[:,1]))]
sigma1 = (Obs_data1_log10yerror[:][0] +  Obs_data1_log10yerror[:][0])/2

OD1 = [Obs_data1.transpose(), HIST1_bins,sigma1,"Willott"]

###########################################################################

HIST2_bins=[-22.70,-22.27,-21.77,-21.27,-20.77,-20.27,-19.77,-19.27]
Bouwens = array(
[# Mag,LumFunct, +/err #
[-22.52,0.000002,0.000002],
[-22.02,0.000011,0.000004],
[-21.52,0.000029,0.000008],
[-21.02,0.000060,0.000012],
[-20.52,0.000146,0.000023],
[-20.02,0.000296,0.000045],
[-19.52,0.000611,0.000081]
])
Obs_data2 = zeros([7,4])
Obs_data2_log10 = zeros([7,4])
Obs_data2yerror = [array(Bouwens[:,2]),array(Bouwens[:,2])]
Obs_data2xerror = [0.25,0.25,0.25,0.25,0.25,0.25,0.25]
Obs_data2[:,0]=Bouwens[:,0]
Obs_data2[:,1]=Bouwens[:,1]
Obs_data2[:,2]=0
Obs_data2[:,3]=0.25
Obs_data2_log10[:,0]=Bouwens[:,0]
Obs_data2_log10[:,1]=log10(Bouwens[:,1])
Obs_data2_log10[:,2]=0
Obs_data2_log10[:,3]=0.25
Obs_data2yerror[0][0]=0.00000199
Obs_data2_log10yerror = [array(log10(Bouwens[:,1]/(Bouwens[:,1]-Bouwens[:,2]))),
                         array(log10((Bouwens[:,1]+Bouwens[:,2])/Bouwens[:,1]))]
Obs_data2_log10yerror[0][0]=0.30103
sigma2 = (Obs_data2_log10yerror[:][0] + Obs_data2_log10yerror[:][1] )/2

OD2 = [Obs_data2.transpose(), HIST2_bins,sigma2,"Bouwens"]

###########################################################################

HIST3_bins=[-22.38,-21.87,-21.62,-21.37,-21.12,-20.87,-20.63]
McLure = array(
[# Mag,LumFunct, Lowerror, Uperror #
[-22.12,10**(-5.886),10**(-6.747),10**(-5.617)],
[-21.75,10**(-5.097),10**(-5.406),10**(-4.918)],
[-21.50,10**(-4.910),10**(-5.154),10**(-4.756)],
[-21.25,10**(-4.463),10**(-4.593),10**(-4.357)],
[-21.00,10**(-4.162),10**(-4.260),10**(-4.081)],
[-20.75,10**(-3.918),10**(-4.024),10**(-3.837)]
])

Obs_data3 = zeros([6,4])
Obs_data3_log10 = zeros([6,4])

Obs_data3yerror = [array(McLure[:,1]-McLure[:,2]),array(McLure[:,3]-McLure[:,1])]
Obs_data3xerror = [0.25,0.125,0.125,0.125,0.125,0.125]
Obs_data3[:,0]=McLure[:,0]
Obs_data3[:,1]=McLure[:,1]
Obs_data3[:,2]=0
Obs_data3[:,3]=0.25
Obs_data3_log10[:,0]=McLure[:,0]
Obs_data3_log10[:,1]=log10(McLure[:,1])
Obs_data3_log10[:,2]=0
Obs_data3_log10[:,3]=0.25

Obs_data3_log10yerror = [array(log10(McLure[:,1]/McLure[:,2])),array(log10(McLure[:,3]/McLure[:,1]))]
sigma3 = ( Obs_data3_log10yerror[:][0]+Obs_data3_log10yerror[:][1])/2

OD3 = [Obs_data3.transpose(), HIST3_bins,sigma3,"McLure"]

###########################################################################

HIST4_bins=[-22.25,-21.75,-21.25,-20.75,-20.25,-19.75,-19.25]#,-18.75]
# Finkelstein et al - 2014
Finkelstein = array(
[#Mag, LumFunct, up_error, low_error
[-22.0, 0.0091*0.001, +0.0057*0.001,	-0.0039*0.001],
[-21.5, 0.0338*0.001, +0.0105*0.001,	-0.0085*0.001],
[-21.0, 0.0703*0.001, +0.0148*0.001,	-0.0128*0.001],
[-20.5, 0.1910*0.001, +0.0249*0.001,	-0.0229*0.001],
[-20.0, 0.3970*0.001, +0.0394*0.001,	-0.0357*0.001],
[-19.5, 0.5858*0.001, +0.0527*0.001,	-0.0437*0.001]
#,[-19.0, 0.8375*0.001, +0.0916*0.001,	-0.0824*0.001]
])

Obs_data4 = zeros([6,4])
Obs_data4_log10 = zeros([6,4])
                              #  Lower error               , Upper error
Obs_data4yerror = [array(Finkelstein[:,1]+Finkelstein[:,3]), array(Finkelstein[:,1]+Finkelstein[:,2])]
Obs_data4xerror = [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]

Obs_data4[:,0] = Finkelstein[:,0]
Obs_data4[:,1] = Finkelstein[:,1]
Obs_data4[:,2] = 0
Obs_data4[:,3] = 0.25

Obs_data4_log10[:,0] = Finkelstein[:,0]
Obs_data4_log10[:,1] = log10(Finkelstein[:,1])
Obs_data4_log10[:,2] = 0
Obs_data4_log10[:,3] = 0.25

Obs_data4_log10yerror = [array(log10(Finkelstein[:,1]/(Finkelstein[:,1]+Finkelstein[:,3]))),
                         array(log10((Finkelstein[:,1]+Finkelstein[:,2])/Finkelstein[:,1]))]
sigma4 = (Obs_data4_log10yerror[:][0] + Obs_data4_log10yerror[:][1])/2

OD4 = [Obs_data4.transpose(), HIST4_bins,sigma4,"Finkelstein"]
