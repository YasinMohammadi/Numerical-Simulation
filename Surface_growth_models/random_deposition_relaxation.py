import numpy as np
import matplotlib.pyplot as plt

def square_rdr(time_step, ensemble, sqr_len):

    h_variance = np.zeros(time_step)

    for tries in range(ensemble):

        h = np.zeros((sqr_len, sqr_len))

        for time_var in range(time_step):
            for position_var in range(sqr_len ** 2):

                random_var = np.random.randint(sqr_len, size=2)

                random_var = np.random.randint(sqr_len, size=2)
                hhh = np.array([[h[random_var[0]-1][random_var[1]-1],h[random_var[0]-1][random_var[1]],h[random_var[0]-1][(random_var[1]+1)%sqr_len]],\
                    [h[random_var[0]][random_var[1]-1],h[random_var[0]][random_var[1]]+1,h[random_var[0]][(random_var[1]+1)%sqr_len]],\
                        [h[(random_var[0]+1)%sqr_len][random_var[1]-1],h[(random_var[0]+1)%sqr_len][random_var[1]],h[(random_var[0]+1)%sqr_len][(random_var[1]+1)%sqr_len]]])
                        

                min_hhh = np.min(hhh)

                if (h[random_var[0]][random_var[1]] == min_hhh):
                    h[random_var] += 1
                else:
                    additive = np.array(np.unravel_index(hhh.argmin(), hhh.shape))
                    h[(additive + random_var - 1)%sqr_len] += 1

            h_variance[time_var] += (np.var(h))**(0.5)
    h_variance = h_variance/ensemble

    return h_variance

time_step = 1000
ensemble = 25
result = []

for Len_var in range(3,11):
    
    sqr_len = 2**Len_var    
    square_rdr_var = square_rdr(time_step, ensemble, sqr_len)
    result.append(square_rdr_var)
    time_axis = np.arange(0,time_step)
    plt.loglog(time_axis,square_rdr_var)

    

plt.xlabel('Time') 
plt.ylabel('Ensemble Mean Variance') 
plt.title('Random Deposition with Surface Relaxation') 
plt.show() 

np.savetxt("resultRDR.csv", result, delimiter=",")


                        
                

                
            
 