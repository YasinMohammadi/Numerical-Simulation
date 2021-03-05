import matplotlib.pyplot as plt 
import numpy as np
from scipy.ndimage import measurements


def Avalanches(N, p, count):
    Medium = np.random.choice(a=[0, 1], size=(N, N), p=[p, 1-p])
    Medium[int(N/2),int(N/2)] = 2

    clusterLenArr = []
    clusterRadiudArr = []


    
    for counter in range(count):        
        for Avalanche in reversed(range(N)):
            clusterLen = (np.count_nonzero(Medium == 2))
            Radius = clusterLen ** 0.5
            randCol = np.random.choice(\
                np.arange(start = int(N/2)-int(Radius+1),stop = int(N/2)+int(Radius+1),step = 1), size= 2) # to choose a random area
            if 2 in Medium[randCol[0]-2:randCol[0]+3, randCol[1]-2:randCol[1]+3]:
                np.place((Medium[randCol[0]-2:randCol[0]+3, randCol[1]-2:randCol[1]+3]),\
                    (Medium[randCol[0]-2:randCol[0]+3, randCol[1]-2:randCol[1]+3]) == 1,\
                        2)                      


                break



    
        if ((counter%N)==0):
            clusterLenArr.append(clusterLen)
            clusterRadiudArr.append(Radius)
            plt.imshow(Medium, origin="lower")
            plt.savefig('EMG {0}.jpg'.format((N,p, counter)))
            plt.close()

    return clusterLenArr, clusterRadiudArr

for i in range(4,9):
    for p in range(1,9,1):
        Leng, Rad = Avalanches(2**i, p/10, 4**i)
        np.savetxt('Length{0}.csv'.format((2**i,p/10)), Leng, delimiter=",")
        np.savetxt('Radius{0}.csv'.format((2**i,p/10)), Rad, delimiter=",")


