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

    def __init__(self, name, capital):
        self.prob = LpProblem(name, LpMaximize)
        self.x = []
        self.vars = None
        self.coeff = None
        self.capital = capital
        self.left_values = []

    def add_variable(self, name):
        self.x.append(name)
        self.x.append("mul_{}".format(name))

    def save_variables(self):
        self.vars = LpVariable.dicts("vars", self.x, 0, cat=LpInteger)
        #self.coeff = np.zeros((1, len(self.x)))

    def add_products(self, products):
        objetive = []
        capital = []
        for p in products:
            self.add_variable(p['name'])
            objetive += [p['yield'], 0]
            capital += [1, 0]

        self.save_variables()
        #self.coeff = np.array(objetive)
        #self.coeff = np.vstack([self.coeff, capital])
        self.coeff = np.array(capital)

        for v, c in zip(self.vars, objetive):
            print(v, c)
        self.prob += lpSum([self.vars[v] * c for v, c in zip(self.x, objetive)]), "maximize"

        for p in products:
            constraint = self.get_multiple_constraint(p)
            self.coeff = np.vstack([self.coeff, constraint])
        # for i, coefficient in enumerate(self.coeff):
        #     if i == 0:
        #         self.prob += lpSum([self.vars[v] * float(c) for v, c in zip(self.x, coefficient)]) == 0, "constraint {}".format(i)
        #     else:
        #         self.prob += lpSum([self.vars[v] * int(c) for v, c in zip(self.x, coefficient)]) == 0, "constraint {}".format(i)

        self.prob += lpSum([self.vars[v] * float(c) for v, c in zip(self.x, self.coeff[0])]) <= self.capital, "capital"
        self.prob += lpSum([self.vars[v] * float(c) for v, c in zip(self.x, self.coeff[1])]) == 0, "multiple 1"
        self.prob += lpSum([self.vars[v] * float(c) for v, c in zip(self.x, self.coeff[2])]) == 0, "multiple 2"

    def get_multiple_constraint(self, product):
        constraint = np.zeros(len(self.x))
        var_index = self.x.index(product['name'])
        constraint[var_index] = 1
        constraint[var_index + 1] = -product['increment']
        return constraint

    def add_constraint(self, coefficients, operator, left_value, name):
        self.coeff = np.vstack([self.coeff, coefficients])
        self.left_values.append({
            "op": operator,
            "left": left_value,
            "name": name
        })

    def apply_constraints(self,):
        for i, c in enumerate(self.coeff):
            if self.left_values[i]['op'] == '==':
                self.prob += lpSum(
                    [self.vars[v] * float(c) for v, c in zip(self.x, c)]) == self.left_values[i]['left'],\
                             self.left_values[i]['name']
            elif self.left_values[i]['op'] == '<=':
                self.prob += lpSum(
                    [self.vars[v] * float(c) for v, c in zip(self.x, c)]) <= self.left_values[i]['left'],\
                             self.left_values[i]['name']


