import numpy as np

def square_generalMC(rnd_sample, shape_range, shape_base, Error, min_step, max_step): #square_generalMC represents ....
    #.... a general function for Monte Carlo Integration with a sqare(ic) sapace of test 

    flag        = 1
    counter     = 0
    in_function = 0
    con_facor   = 0 #if = 1 then converged else diverged
    Dimension = rnd_sample

    Ans = None

    while flag == 1:

        Test = (shape_range * np.random.random_sample(size = rnd_sample)) - shape_base
        TestFunction = Function(Test)

        if TestFunction <= 0: #Surface is also included in integration
            in_function += 1
            #end if

        if counter >= 2:
            preAns = Ans            
            #end if
        if counter >= 1:
            Ans = (in_function / counter) * ((shape_range - shape_base) ** Dimension)
            #end if


        
        

        if counter >= min_step:
            
            func_error = ((Ans - preAns) ** 2) ** 0.5  #Used to determin abs of Error
            if func_error <= Error :
                flag = 0
                con_facor = 1
            elif counter == max_step:
                flag = 0
                #End if
            #End if
                    

        counter += 1       
        

        #end while



    return con_facor, Ans

rnd_sample = 5 
shape_range = 20
shape_base = 0 
Error = (0.01) 
min_step = 300000 
max_step = 100000000

X = square_generalMC(rnd_sample, shape_range, shape_base, Error, min_step, max_step)
print(X)

