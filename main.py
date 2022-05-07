# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import gurobipy as gp
import matplotlib.pyplot as pyplot
from gurobipy import GRB
import numpy as np
import scipy.sparse as sp

try:
    # model = gp.Model("mip1")
    #
    # x = model.addVar(vtype=GRB.BINARY, name="x")
    # y = model.addVar(vtype=GRB.BINARY, name="y")
    # z = model.addVar(vtype=GRB.BINARY, name="z")
    #
    # model.setObjective(x + y + 2*z, GRB.MAXIMIZE)
    #
    # model.addConstr(x + 2*y + 3*z <= 4, "c0")
    # model.addConstr(x + y >= 1, "c1")
    #
    # model.optimize()
    #
    # for v in model.getVars():
    #     print('%s %g' % (v.VarName, v.X))
    #
    # print('Obj: %g' % model.ObjVal)

    # m = gp.Model("matrix1")
    # x = m.addMVar(shape=3, vtype=GRB.BINARY, name="x")
    # obj = np.array([1.0, 1.0, 2.0])
    # m.setObjective(obj @ x, GRB.MAXIMIZE)
    #
    # val = np.array([1.0, 2.0, 3.0, -1.0, -1.0])
    # row = np.array([0, 0, 0, 1, 1])
    # col = np.array([0, 1, 2, 0, 1])
    #
    # A = sp.csr_matrix((val, (row, col)), shape=(2,3))
    # rhs = np.array([4.0, -1.0])
    # m.addConstr(A @ x <= rhs, name="c")
    #
    # m.optimize()
    #
    # print(x.X)
    # print('Obj: %g' % m.ObjVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')

