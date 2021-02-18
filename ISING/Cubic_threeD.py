import numpy as np
import random

def total_energy_3d(Lattice, interaction): 
    #To calculate total Energy of System
    #interaction == J
    L = len(Lattice)
    energy = 0 
    for I in range(L):
        for J in range(L):
            for K in range(L):
                energy += Lattice[I][J][K] * (Lattice[(I+1)%L][J][K] + Lattice[I-1][J][K] + \
                    Lattice[I][(J+1)%L][K] + Lattice[I][J-1][K] + \
                        Lattice[I][J][(K+1)%L] + Lattice[I][J][K-1])
    total_energy = interaction * energy

    return total_energy


def metropolis_cubic_3d(Lattice, Temp, interaction):

    monteCarlo_Steps = 1000
    K = 1
    beta = 1 / (K * Temp)

    exp_cte = beta * interaction * 2
    
    L = len(Lattice)
    rept = monteCarlo_Steps * (L ** 2)

    for I in range(rept):
        X=np.random.randint(L, size=(3))
        energy = Lattice[(X[0])][(X[1])][(X[2])] * (Lattice[((X[0]+1)%L)][(X[1])][(X[2])] + Lattice[(X[0]-1)][(X[1])][(X[2])] + \
            Lattice[X[0]][((X[1]+1)%L)][(X[2])] + Lattice[(X[0])][(X[1]-1)][(X[2])] + \
                Lattice[(X[0])][(X[1])][((X[2]+1)%L)] + Lattice[(X[0])][(X[1])][(X[2]-1)])

        if (energy<=0) or (random.random()<(np.exp(-(exp_cte * energy)))):
            Lattice[X[0]][X[1]][X[2]] = -Lattice[X[0]][X[1]][X[2]]

    return Lattice



def magnetization(Lattice, Temp, interaction, Step):
    magnt = []
    for I in range(Step):
        magnt.append(np.mean(Lattice))
        Lattice = metropolis_cubic_3d(Lattice, Temp, interaction)

    return  magnt


temp = np.arange(4,5,0.1)
Step = 100
interaction = 1

for len_var in range(2, 5):
    L = 2 ** len_var
    Magnetization = []
    Susceptibility = []
    for Temp in (temp):

        Lattice = np.full((L, L, L), 1)
        Mag = magnetization(Lattice, Temp, interaction, Step)

        Magnetization.append(np.mean(Mag)/Temp)
        Susceptibility.append(np.var(Mag)/Temp)

    with open('Magnetization.csv', 'a') as result:
        np.savetxt(result, Magnetization, delimiter='\n ', newline=', ')
        result.write("\n")

    with open('Susceptibility.csv', 'a') as result:
        np.savetxt(result,Susceptibility, delimiter='\n ', newline=', ')
        result.write("\n")


