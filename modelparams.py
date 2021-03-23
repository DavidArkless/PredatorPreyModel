import numpy as np


UPTAKE_VELOCITY = 5
SATURATION_CONSTANT = 1.5
YIELD = 10



parameters = {
    "velocity": UPTAKE_VELOCITY,  # Maximum number of prey
    "K": SATURATION_CONSTANT,  # Maximum number of predators
    "yield": YIELD, # Reproduction rate of prey

}

"""
Jacob-Monod Model

dxdt = Vy / (K + y)

C = x + Yield * y

dxdt = V(C - x) / (YK + (C- x))

dydt = -1/Y * Vy / (K + y)
"""

initial_values = [[400, 28]]

time = np.linspace(0, 100, num=1000)


def dxdt(prey_pop, predator_pop, params):

    C = prey_pop + params['yield'] * predator_pop

    prey = (params['velocity'] * (C - prey_pop)) / (params['K'] + (C - prey_pop))


    return prey


def dydt(prey_pop, predator_pop, params):

    predator = -1 / params['yield'] * (params['velocity'] * predator_pop) / (params['K'] + predator_pop)

    return predator