import runge_kutta

def dudy(U, y): 
    g = 9.806
    c = 1
    m = 1 
    alph = 2 #power of drag (drag = -c**2*(U**(alpha)))

    duydy = -((g/U)+((c**2)/m)*(U**(alph - 1)))

    return duydy
    #End def

def duds(U, x): 
    g = 9.806
    c = 1
    m = 1 
    alph = 2 #power of drag (drag = -c**2*(U**(alpha)))

    duxdx = -((c**2)/m)*(U**(alph - 1))

    return duxdx
    #End def