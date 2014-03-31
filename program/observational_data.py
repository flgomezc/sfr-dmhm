from numpy import *

HIST1_bins=[-22.75,-22.25,-21.75,-21.25,-20.75,-20.25]

Willott = array( 
[# Mag,LumFunct, low_err, upp_err #
[-22.5, 2.66E-8, 9.08E-9, 7.78E-8],
[-22.0, 2.18E-6, 8.70E-7, 9.70E-6],
[-21.5, 1.45E-5, 2.88E-6, 2.92E-5],
[-21.0, 1.29E-4, 7.06E-5, 2.19E-4],
[-20.5, 2.30E-4, 9.34E-5,5.77E-4]
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


HIST2_bins=[-22.70,-22.27,-21.77,-21.27,-20.77,-20.27,-19.77,-19.27,-18.27,-17.27,-16.27]
Bouwens = array( 
[# Mag,LumFunct, +/err #
[-22.52,0.000002,0.000002],
[-22.02,0.000011,0.000004],
[-21.52,0.000029,0.000008],
[-21.02,0.000060,0.000012],
[-20.52,0.000146,0.000023],
[-20.02,0.000296,0.000045],
[-19.52,0.000611,0.000081],
[-18.77,0.000860,0.000150],
[-17.77,0.002920,0.000650],
[-16.77,0.004710,0.001490]
])  

Obs_data2 = zeros([10,4])
Obs_data2_log10 = zeros([10,4])

Obs_data2yerror = [array(Bouwens[:,2]),array(Bouwens[:,2])]
Obs_data2xerror = [0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,0.5,0.5]
Obs_data2[:,0]=Bouwens[:,0]
Obs_data2[:,1]=Bouwens[:,1]
Obs_data2[:,2]=0
Obs_data2[:,3]=0.25
Obs_data2_log10[:,0]=Bouwens[:,0]
Obs_data2_log10[:,1]=log10(Bouwens[:,1])
Obs_data2_log10[:,2]=0
Obs_data2_log10[:,3]=0.25
Obs_data2yerror[0][0]=0.00000199

Obs_data2_log10yerror = [array(log10(Bouwens[:,2])),array(log10(Bouwens[:,2]))]



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
