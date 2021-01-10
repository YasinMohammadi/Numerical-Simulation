import numpy as np
import matplotlib.pyplot as plt

def square_bd(time_step, ensemble, sqr_len):

    h_variance = np.zeros(time_step)

    for tries in range(ensemble):

        h = np.zeros((sqr_len,sqr_len))
        
        for time_var in range(time_step):
            for horizontal_var in range(sqr_len):
                for vertical_var in range(sqr_len):

                    random_var = np.random.randint(sqr_len, size=2)
                    hhh = [h[random_var[0]-1][random_var[1]-1],h[random_var[0]-1][random_var[1]],h[random_var[0]-1][(random_var[1]+1)%sqr_len],\
                        h[(random_var[0]+1)%sqr_len][random_var[1]-1],h[(random_var[0]+1)%sqr_len][random_var[1]],h[(random_var[0]+1)%sqr_len][(random_var[1]+1)%sqr_len],\
                            h[random_var[0]][random_var[1]-1],h[random_var[0]][random_var[1]]+1,h[random_var[0]][(random_var[1]+1)%sqr_len]]

                    h[random_var[0]][random_var[1]] = np.max(hhh)

            h_variance[time_var] += (np.var(h))**(0.5)

    h_variance = h_variance/ensemble

    return h_variance



def linear_bd(time_step, ensemble, line_len):

    varh = np.zeros(time_step)
    for rea in range(ensemble):
    
        h = np.zeros(line_len) 
        for t in range(time_step):
            for x in range(line_len):        
                xrandom = np.random.randint(0,line_len)
                hhh = [h[xrandom-1],h[(xrandom+1)%line_len],h[xrandom]+1]
                h[xrandom] = np.max(hhh)
                
            varh[t] += (np.var(h))**(0.5)
           
    varh = varh/ensemble
    return varh



time_step = 10000
ensemble = 100
result = []

for Len_var in range(3,11):
    sqr_len = 2**Len_var    
    square_bd_var = square_bd(time_step, ensemble, sqr_len)
    result.append(square_bd_var)
    time_axis = np.arange(0,time_step)
    plt.loglog(time_axis,square_bd_var)

plt.xlabel('Time') 
plt.ylabel('Ensemble Mean Variance') 
plt.title('Ballistic Deposition') 
plt.show() 

np.savetxt("result.csv", result, delimiter=",")

  
