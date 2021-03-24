import numpy as np



K_PREY = 1500 # max prey
# K_PREDATOR = 46 # max predator
ALPHA = 1 # prey reproduction rate
BETA = 1 # predation rate
GAMMA = 0.2 # predator reproduction rate
DELTA = 0.3 # predator competition rate
B = 5 # controls how rapidly an individual predator becomes full






parameters = {
    "prey_max": K_PREY,  # Maximum number of prey
    # "predator_max": K_PREDATOR,  # Maximum number of predators
    "alpha": ALPHA,
    "beta": BETA,
    "gamma": GAMMA,
    "delta": DELTA,
    "b": B,

}

"""
Rosenzweig and MacArthur model
https://www.cs.bham.ac.uk/~szh/teaching/matlabmodeling/Lecture6_body.pdf

dx/dt = x(A(1 - x/K)- B y/(b+x))
dy/dt = -y(G - D(x/(b+x)))


"""

initial_values = [[400, 28]]

time = np.linspace(0, 100, num=1000)


def dxdt(prey_pop, predator_pop, params):

    prey = prey_pop * (params['alpha'] * (1 - prey_pop / params['prey_max']) -
                       params['beta'] * predator_pop / (params['b'] + prey_pop))




    return prey


def dydt(prey_pop, predator_pop, params):

    predator = -predator_pop * (params['gamma'] - params['delta'] * prey_pop/(params['b'] + prey_pop))



    return predator