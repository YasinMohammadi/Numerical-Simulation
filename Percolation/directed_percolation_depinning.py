import matplotlib.pyplot as plt 
import numpy as np
from scipy.ndimage import measurements



def DPD(N, p, count):
    Medium = np.random.choice(a=[0, 1], size=(N, N), p=[p, 1-p])
    Medium[0] = 2

    clusterHeight = np.ones(N)
    heightMean = []
    heightVari = []

    
    for counter in range(count):

        randCol = np.random.randint(N) # to choose a random column
        for wet in reversed(range(N)):
            if (Medium[wet][randCol] == 1):
                heightMean.append(np.mean(clusterHeight))
                heightVari.append(np.var(clusterHeight))
                if 2 in Medium[wet-1:(wet+2),(randCol-1):(randCol+2)] \
                    and randCol != 0:
                    Medium[:wet+1,randCol] = 2
                    clusterHeight[randCol] = wet
                    break
                elif 2 in Medium[wet-1:(wet+2),(randCol):(randCol+2)] \
                    and randCol == 0:
                    Medium[:wet+1,randCol] = 2
                    clusterHeight[randCol] = wet
                    break

            #print(heightMean)
    
        if ((counter%N)==0):
            plt.imshow(Medium, origin="lower")
            plt.savefig('EMG {0}.jpg'.format((N,p, counter)))
            plt.close()
        plt.show()
    return heightMean, heightVari

for i in range(9,10):
    for p in range(7,9,1):
        Mean, Var = DPD(2**i, p/10, 4**i)
        np.savetxt('Mean{0}.csv'.format((2**i,p/10)), Mean, delimiter=",")
        np.savetxt('Var{0}.csv'.format((2**i,p/10)), Var, delimiter=",")




