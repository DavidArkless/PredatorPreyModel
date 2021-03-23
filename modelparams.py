import numpy as np


A = 0.23
B = 0.00001
C = 0.82
G = 0.53
M = 0.7


parameters = {
    "A": A,
    "B": B,
    "C": C,
    "G": G,
    "M": M,
}

"""
Arditi-Ginzburg

dx/dt = x(A - Bx) - Cxy/(x+y)

dy/dt = -Gy + Mxy/(x+y)

A,B: controls the growth of the prey w/o predator

C controls how fast the predator consumes the prey

G controls how fast the predator dies w/o prey

M controls how fast the predator grows with maximum prey



Need to some how link the growth of prey 
and predators so that they affect each other

"""

initial_values = [[400, 28]]

time = np.linspace(0, 150, num=100000)


def dxdt(prey_pop, predator_pop, params):

    prey = prey_pop * (params['A'] - params['B'] * prey_pop) - params['C'] \
           * prey_pop * predator_pop / (prey_pop + predator_pop)


    return prey


def dydt(prey_pop, predator_pop, params):

    predator = - params['G'] * predator_pop + params['M'] * prey_pop * predator_pop / (prey_pop + predator_pop)

    return predator