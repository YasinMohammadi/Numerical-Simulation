import numpy as np
import monte_carlo_integration as MC
import riemann_sum_integration as riemann



def Function(Var):
    
    mathFunction = Var[0]**2 + Var[1]**2 + Var[2]**2 + Var[3]**2 + Var[4]**2 - Var[5]**2
    
    return mathFunction

Dimension = 5 
shape_range = 5 
shape_base = 0 
Error = (10e-5) 
min_step = 300 
max_step = 10000

mc_ans = MC.square_generalMC(rnd_sample, shape_range, shape_base, Error, min_step, max_step)


integral_range = [1.0,1.0,1.0,1.0,1.0]
Step = 10
riemann_ans = riemann.five_var(integral_range, Step)



