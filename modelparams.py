import numpy as np



def alpha_sin(x):
    A = 10000
    K = 1

    food_rate = A * np.sin(K * x) + 2 * A

    return food_rate



ALPHA = 0.4   # Prey Reproduction rate
BETA = 0.07 / 4  # Predation rate
DELTA = 0.005 / 4  # Predator Reproduction/ food rate
GAMMA = 0.3 * 4 # Competition Rate

parameters = {
    "alpha": ALPHA,  # Prey Reproduction rate
    "beta": BETA,  # Predation rate
    "delta": DELTA,  # Predator Reproduction / food rate
    "gamma": GAMMA,  # Competition Rate
}

initial_values = [[400, 28]]

time = np.linspace(0, 100, num=1000)


def dxdt(x, y, params):

    prey = params['alpha'] * x - params['beta'] * x * y

    return prey


def dydt(x, y, params):

    predator = params['delta'] * x * y - params['gamma'] * y

    return predator