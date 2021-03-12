import matplotlib.pyplot as plt
plt.style.use('ggplot')


def draw_prey_predator_graphs(data):
    for index, modelData in enumerate(data):
        preyLine = plt.plot(modelData.t, modelData.solution[:, 0], label="prey")
        predatorLine = plt.plot(modelData.t, modelData.solution[:, 1], label="predator")

        plt.plot()
        plt.xlabel("Time")
        plt.ylabel("Population (Hundreds)")
        plt.legend()
        plt.savefig(f"graphs/{modelData.y0[0]}-{modelData.y0[1]}PreyPredatorGraphs.jpg")
        plt.show()
        plt.close()


def draw_phase_space_plot(data):
    for index, modelData in enumerate(data):
        preyPredatorLine = plt.plot(modelData.solution[:, 0], modelData.solution[:, 1],
                                    label=f"Initial Values:{modelData.y0[0]}:{modelData.y0[1]}")

    plt.xlabel("Prey (Hundreds)")
    plt.ylabel("Predator (Hundreds)")
    plt.legend()
    plt.title("Predator Prey Model Phase Plot")
    plt.savefig(f"graphs/PredatorPreyModelPhasePlot.jpg")
    plt.show()
    plt.close()
