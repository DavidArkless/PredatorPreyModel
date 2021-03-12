import numpy as np

import predatorpreymodel as model
import drawgraphs


def main():
    results = list()

    time = np.linspace(0, 100, num=1000)

    alpha = 2 / 3  # Prey Reproduction rate
    beta = 4 / 3  # Predation rate
    delta = 1  # Predator Reproduction/ food rate
    gamma = 1  # Competition Rate

    parameters = {
        "alpha": alpha,  # Prey Reproduction rate
        "beta": beta,  # Predation rate
        "gamma": gamma,  # Predator Reproduction/ food rate
        "delta": delta  # Competition Rate
    }

    initial_values = [[0.9, 0.9], [1, 1], [1.1, 1.1], [1.2, 1.2]]

    for i, vals in enumerate(initial_values):
        result = model.PredatorPreyModel(vals, time, parameters)

        results.append(result)

    drawgraphs.draw_prey_predator_graphs(results)
    drawgraphs.draw_phase_space_plot(results)


if __name__ == '__main__':
    main()
