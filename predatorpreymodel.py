import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve


class PredatorPreyModel:

    def __init__(self, y0, t, params):
        self.y0 = y0
        self.t = t
        self.params = params
        self.model = PredatorPreyModel.model(self.y0, self.t, self.params)
        self.solution = self.solve_model()
        self.fixedPoints = self.get_fixed_points()

    def __str__(self):
        return f"With initial conditions {self.y0} and parameters \nalpha : {self.params['alpha']}" \
               f"\nbeta : {self.params['beta']}\ndelta: {self.params['delta']}\ngamma: {self.params['gamma']}" \
               f"\nthe solution to the model is {self.solution} and the fixed points are {self.fixedPoints}"

    @staticmethod
    def model_equations(p, params):

        x, y = p
        dxdt = params['alpha'] * x - params['beta'] * x * y
        dydt = params['delta'] * x * y - params['gamma'] * y

        return dxdt, dydt

    def get_fixed_points(self):

        fixedPoints = list()

        for i in range(50):

            if len(fixedPoints) == 2:
                break

            initialGuess = np.array([i, i])

            solution = fsolve(PredatorPreyModel.model_equations, initialGuess, args=(self.params,))

            solution = np.ndarray.tolist(solution)

            if not (solution in fixedPoints):
                fixedPoints.append(solution)

        return fixedPoints

    @staticmethod
    def model(y0, t, params):

        x = y0[0]
        y = y0[1]

        dxdt = params['alpha'] * x - params['beta'] * x * y
        dydt = params['delta'] * x * y - params['gamma'] * y

        model = [dxdt, dydt]

        return model

    def solve_model(self):

        solution = odeint(PredatorPreyModel.model, self.y0, self.t, args=(self.params,))

        return solution