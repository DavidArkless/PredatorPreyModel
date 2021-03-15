import matplotlib.pyplot as plt
import os
plt.style.use('ggplot')


def draw_prey_predator_graphs(data):

    if not os.path.exists("graphs"):
        os.makedirs("graphs")

    for index, modelData in enumerate(data):
        preyLine = plt.plot(modelData.t, modelData.solution[:, 0], label="prey")
        predatorLine = plt.plot(modelData.t, modelData.solution[:, 1], label="predator")


        plt.plot()
        plt.title("Population Of Moose And Wolves Over Time")
        plt.xlabel("Time")
        plt.ylabel("Population (Hundreds)")
        plt.legend()
        plt.savefig(f"graphs/{modelData.y0[0]}-{modelData.y0[1]}PreyPredatorGraphs.jpg")
        plt.show()
        plt.close()


    for index, modelData in enumerate(data):
        fig, (ax1, ax2) = plt.subplots(2)

        fig.suptitle("Population Of Moose And Wolves Over Time")



        preyLine, = ax1.plot(modelData.t, modelData.solution[:, 0], label="prey")
        predatorLine, = ax2.plot(modelData.t, modelData.solution[:, 1], label="predator", color="#348ABD")
        




        ax1.set_ylabel("Moose (Hundreds)")
        ax2.set_ylabel("Wolves (Hundreds)")



        plt.xlabel("Time")


        plt.savefig(f"graphs/{modelData.y0[0]}-{modelData.y0[1]}PreyPredatorSubPlotGraphs.jpg")
        plt.show()
        plt.close()


def draw_phase_space_plot(data):
    for index, modelData in enumerate(data):
        preyPredatorLine = plt.plot(modelData.solution[:, 0], modelData.solution[:, 1],
                                    label=f"Initial Values:{modelData.y0[0]}:{modelData.y0[1]}")

    plt.xlabel("Moose (Hundreds)")
    plt.ylabel("Wolves (Hundreds)")
    plt.legend()
    plt.title("Population Of Wolves Against Moose")
    plt.savefig(f"graphs/PredatorPreyModelPhasePlot.jpg")
    plt.show()
    plt.close()
