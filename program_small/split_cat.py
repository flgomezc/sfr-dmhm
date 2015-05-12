import numpy as np

cat = np.loadtxt('../data/P_Bolshoi/z6.cvs',usecols=([3,4,5,6]),
                 delimiter=',', skiprows=1)

catSize = 250 #Mpc h-1
smallcatSize = 125

for i in range(2):
    for j in range(2):
        for k in range(2):
            N = i*2*2 +j*2 +k
            name = '../data/P_Bolshoi/cells/'+str(N)+'.dat'
            smallcat = open(name, 'w')
            index = np.where((cat[:,0]>i*125.0) & (cat[:,0]<(i+1)*125.0) &
                             (cat[:,1]>j*125.0) & (cat[:,1]<(j+1)*125.0) &
                             (cat[:,2]>k*125.0) & (cat[:,2]<(k+1)*125.0))[0]
            aux = cat[index]

            for n in range(index.size):
                smallcat.write(str(aux[n,0])+'\t'+str(aux[n,1])+'\t'
                               +str(aux[n,2])+'\t'+str(aux[n,3])+'\n')
            smallcat.close()
