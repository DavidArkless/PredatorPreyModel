import numpy as np



K_PREY = 1500
PREY_GROWTH = 0.02
PREY_DECAY = 0.05

K_PREDATOR = 46
PREDATOR_GROWTH = 0.05
PREDATOR_DECAY = 0.01


parameters = {
    "prey_max": K_PREY,  # Maximum number of prey
    "predator_max": K_PREDATOR,  # Maximum number of predators
    "prey_growth": PREY_GROWTH, # Reproduction rate of prey
    "predator_growth": PREDATOR_GROWTH, # Reproduction rate of predator
    "prey_decay": PREY_DECAY,
    "predator_decay": PREDATOR_DECAY,

}

"""
Model Combination for periods of different times

So when population of prey and predator are low
We use a logistic growth model

When both populations are high / at max size we use another set of equations to model the 
dramatic decrease
"""

initial_values = [[400, 28]]

time = np.linspace(0, 100, num=1000)


def dxdt(prey_pop, predator_pop, params):

    logistic_growth = (params['prey_growth'] * prey_pop *
                       (1 - prey_pop / (params['prey_max'] - predator_pop)))
    prey = logistic_growth

    return prey


def dydt(prey_pop, predator_pop, params):

    logistic_growth = (params['predator_growth'] * predator_pop *
                       (1 - predator_pop / (params['predator_max'] - prey_pop)))

    # logistic_growth_rounded = np.round_(logistic_growth, decimals=2)
    #
    # if logistic_growth_rounded != 0:
    #     prey = logistic_growth
    #     return prey

    prey = logistic_growth

    return prey