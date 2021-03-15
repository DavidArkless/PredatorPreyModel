import numpy as np

ALPHA = 0.4  # Prey Reproduction rate
BETA = 0.095  # Predation rate
DELTA = 0.7  # Predator Reproduction/ food rate
GAMMA = 0.1  # Competition Rate



parameters = {
    "alpha": ALPHA,  # Prey Reproduction rate
    "beta": BETA,  # Predation rate
    "gamma": GAMMA,  # Predator Reproduction / food rate
    "delta": DELTA  # Competition Rate
}

initial_values = [[0.9, 0.9], [1, 1], [1.1, 1.1], [1.2, 1.2]]  # [prey population, predator population] (Hundreds)

time = np.linspace(0, 100, num=10000)


def dxdt(x, y, params):
    prey = params['alpha'] * x - params['beta'] * x * y

    return prey


def dydt(x, y, params):
    predator = params['delta'] * x * y - params['gamma'] * y

    return predator
