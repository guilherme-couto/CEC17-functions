import cec2017.functions as functions
import numpy as np

class CECProb:
    def __init__(self, dim, func_id):
        self.dim = dim
        self.ub = 100
        self.lb = -100
        self.func_id = func_id

    def fitness(self, x):
        func = functions.all_functions[self.func_id]
        x = np.array(x)
        x.shape = (1,self.dim)
        return func(x)

    def get_bounds(self):
        return ([self.lb]*self.dim, [self.ub]*self.dim)
