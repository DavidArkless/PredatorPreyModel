import numpy as np



def alpha_sin(x):
    A = 10000
    K = 1

    food_rate = A * np.sin(K * x) + 2 * A

    return food_rate



ALPHA = 2 / 3  # Prey Reproduction rate
BETA = 4 / 3  # Predation rate
DELTA = 1  # Predator Reproduction/ food rate
GAMMA = 1  # Competition Rate

parameters = {
    "alpha": ALPHA,  # Prey Reproduction rate
    "beta": BETA,  # Predation rate
    "gamma": GAMMA,  # Predator Reproduction / food rate
    "delta": DELTA  # Competition Rate
}

initial_values = [[0.9, 0.9], [1, 1], [1.1, 1.1], [1.2, 1.2]]

time = np.linspace(0, 100, num=1000)


def dxdt(x, y, params):

    prey = params['alpha'] * x - params['beta'] * x * y

    return prey


def dydt(x, y, params):

    predator = params['delta'] * x * y - params['gamma'] * y

    return predator