import numpy as np
from cy.cymatrix import Multiply as mc
from py.pymatrix import Multiply as mp
import time

n=1000

print("Initialising arrays with dimension {}x{}\n".format(n,n))
a = np.random.rand(n,n)
b = np.random.rand(n,n)

print("Starting Cy...\n")
t0 = time.time()
cy = mc(a,b)
t1 = time.time()

totalcy = t1-t0

print("Starting Py...\n")
t0 = time.time()
py = mp(a,b)
t1 = time.time()

totalpy = t1-t0

print("Checking arrays...\n")
for i in range(n):
    for j in range(n):
        if (cy[i][j]!=py[i][j]):
            print("found mismatch in arrays!\n")
            

print("Cython: {:.5f}\nPython: {:.5f}\n".format(totalcy,totalpy))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))

