import predatorpreymodel as model
import drawgraphs
import modelparams


def main():
    results = list()

    for i, vals in enumerate(modelparams.initial_values):
        result = model.PredatorPreyModel(vals, modelparams.time, modelparams.parameters)

        results.append(result)

    drawgraphs.draw_prey_predator_graphs(results)
    drawgraphs.draw_phase_space_plot(results)


if __name__ == '__main__':
    main()
