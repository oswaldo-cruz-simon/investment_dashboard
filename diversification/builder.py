import numpy as np
from pulp import *

{
    "name": "cumplo",
    "max": 50000,
    "min": 1000,
    "increment": 1000,
    "yield": 0.18
}


class DiversificationBuilder(object):

    def __init__(self, name):
        self.prob = LpProblem("Investment problem", LpMaximize)
        self.x = []
        self.vars = None
        self.coeff = None

    def add_variable(self, name):
        self.x.append(name)
        self.x.append("mul_{}".format(name))

    def save_variables(self):
        self.vars = LpVariable.dicts("vars", self.x, 0)
        self.coeff = np.zeros((1, len(self.x)))

    def add_products(self, products):
        objetive = []
        capital = []
        for p in products:
            self.add_variable(p['name'])
            objetive += [p['yield'], 0]
            capital += [1, 0]

        self.save_variables()
        self.coeff = np.vstack([self.coeff, objetive])
        self.coeff = np.vstack([self.coeff, capital])
