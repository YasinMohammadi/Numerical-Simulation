import numpy as np


def five_var(integral_range, Step):

    varible_num = 5

    #Var = integral_range[0]
    Var = [0.0,0.0,0.0,0.0,0.0]
    deltaVar = np.random.random_sample(varible_num)
    for counter in range(5): 
        #deltaVar[counter] = (integral_range[1][counter] - integral_range[0][counter]) / Step
        deltaVar[counter] = (integral_range[counter]) / Step
        #End for

    Delta = (deltaVar[0] * deltaVar[1] * deltaVar[2] * deltaVar[3] * deltaVar[4])
    



    #for a,b,c in itertools.product(cc1, cc2, cc3):


    sum = 0
    for target_list_i in range(Step):
        Var[0] += deltaVar[0]
        for target_list_j in range(Step):
            Var[1] += deltaVar[1]
            for target_list_k in range(Step):
                Var[2] += deltaVar[2]
                for target_list_m in range(Step):
                    Var[3] += deltaVar[3]
                    for target_list_n in range(Step):
                        Var[4] += deltaVar[4]
                            
                            	
                            
                        #if Function(Var) >= 0: #Surface is also included in integration
                        sum += Delta * Function(Var)
                            #End if

                            
                        #End for
                    #End for
                #End for
            #End for
        #End for

    return sum
    #End Function


#integral_range = [[0.0,0.0,0.0,0.0,0.0],[1.0,1.0,1.0,1.0,1.0]]
integral_range = [1.0,1.0,1.0,1.0,1.0]

Step = 10

X = five_var(integral_range, Step)
print(X)
