import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve


class PredatorPreyModel:
    """
    Class to simulate the predator prey model using Lotka-Volterra equations

    Attributes:
    ------------
        y0: list

            A 1-D list of length 2 contain the two initial values in the format [Prey, Predator)]

        t: numpy.ndarray
            An array that contains all the numbers from n to m in steps of k
            e.g. 10 - 100 in steps of 10 = [10,20,30,40,50,60,70,80,90,100]


        params: dictionary
            A dictionary containing all the parameters that affect how a predator or prey population increase or
            decreases

             {
            "alpha": ALPHA,  # Prey Reproduction rate
            "beta": BETA,  # Predation rate
            "gamma": GAMMA,  # Predator Reproduction / food rate
            "delta": DELTA  # Competition Rate
             }

        model: list
            This list contains the two equations that model the population of the predator and prey

        solution: numpy.ndarray
            Solution is a numpy.ndarray which is a list containing all the values of the population of predator and
            prey at a time t

        fixedPoints: list
            This is a list containing the points at which the population is stable,
             first fixed point: [0,0] (extinction)
             second fixed pot: [n,m] (oscillations)

    Methods:
        model_equations(p, params)
            Static Method
            Used as a helper function to solve for the fixed points which is why it needs the parameter t
            returns the model equations as a list

        get_fixed_points(self)
            returns the solution for the fixed points i.e. when dxdt = 0 and dydt = 0

        model(y0, t, params)
            This also returns the model similarly to model_equation, however is used as a helper function to solve
            for the solutions of the model equations
            returns the model equations

        solve_model(self)
            Finds the solution to the model equations using the helper function model(y0, t, params)
            Returns a list of solutions




    """

    def __init__(self, y0, t, params):

        """

        :param y0:
            The initial values of the population of predator and prey in the format [prey, predator]
        :param t:
            A list of time, that is evenly spaced over a specific interval

        :param params:
            A dictionary that contains the parameters needed to model the predator and prey population
        """
        self.y0 = y0
        self.t = t
        self.params = params
        self.model = PredatorPreyModel.model(self.y0, self.t, self.params)
        self.solution = self.solve_model()
        self.fixedPoints = self.get_fixed_points()

        print(type(self.y0))
        print(type(self.t))
        print(type(self.params))
        print(type(self.model))
        print(type(self.solution))
        print(type(self.fixedPoints))


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