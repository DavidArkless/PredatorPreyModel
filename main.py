import numpy as np

import predatorpreymodel as model
import drawgraphs


def main():
    results = list()

    time = np.linspace(0, 100, num=1000)

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

    for i, vals in enumerate(initial_values):
        result = model.PredatorPreyModel(vals, time, parameters)

        results.append(result)

    drawgraphs.draw_prey_predator_graphs(results)
    drawgraphs.draw_phase_space_plot(results)


if __name__ == '__main__':
    main()
