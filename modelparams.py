import numpy as np


K_PREY = 1500
PREY_GROWTH = 2

K_PREDATOR = 46
PREDATOR_GROWTH = 0.2

PREDATION_RATE = 0.02
COMPETITION_RATE = 0.05



parameters = {
    "prey_max": K_PREY,  # Maximum number of prey
    "predator_max": K_PREDATOR,  # Maximum number of predators
    "prey_growth": PREY_GROWTH, # Reproduction rate of prey
    "predator_growth": PREDATOR_GROWTH, # Reproduction rate of predator
    "predation_rate": PREDATION_RATE,
    "competition_rate": COMPETITION_RATE,
}

"""
Logistic Growth model

dx/dt = rx(1 - x/K)

when x is smaller than K 1 - x / K = 1
When x -> K, (1 - x/K) -> 0

Need to some how link the growth of prey 
and predators so that they affect each other

"""

initial_values = [[400, 28]]

time = np.linspace(0, 100, num=1000)


def dxdt(prey_pop, predator_pop, params):

    logistic_growth = (params['prey_growth'] * prey_pop * (1 - prey_pop / params['prey_max']))

    logistic_decay = 0

    prey = logistic_growth - abs(logistic_decay)


    return prey


def dydt(prey_pop, predator_pop, params):

    logistic_growth = (params['predator_growth'] * predator_pop * (1 - predator_pop / params['predator_max']))

    logistic_decay = 0

    predator = logistic_growth - abs(logistic_decay)

    return predator