import numpy as np


K_PREY = 1500
PREYGROWTH = 2

K_PREDATOR = 46
PREDATORGROWTH = 2



parameters = {
    "prey_max": K_PREY,  # Maximum number of prey
    "predator_max": K_PREDATOR,  # Maximum number of predators
    "prey_growth": PREYGROWTH, # Reproduction rate of prey
    "predator_growth": PREDATORGROWTH, # Reproduction rate of predator
}

"""
Logistic Growth model

dx/dt = rx(1 - x/K)

when x is smaller than K 1 - x / K = 1
When x -> K, (1 - x/K) -> 0

Need to some how link the growth of prey and predators

"""

initial_values = [[400, 28]]

time = np.linspace(0, 25, num=1000)


def dxdt(x, y, params):

    prey = (params['prey_growth'] * x * (1 - x / params['prey_max']))

    return prey


def dydt(x, y, params):

    predator = (params['predator_growth'] * y * (1 - y / params['predator_max']))

    return predator