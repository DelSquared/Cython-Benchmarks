import numpy as np
from cy.cyPi import Pi as cypi
from py.pyPi import Pi as pypi
import time

n=1000000000

print("Finding pi with {} samples".format(n))

print("Starting Cy...\n")
t0 = time.time()
cy = cypi(n)
t1 = time.time()

totalcy = t1-t0

print("Starting Py...\n")
t0 = time.time()
py = pypi(n)
t1 = time.time()

totalpy = t1-t0

print("Cython value = {}\nPython value = {}\n".format(cy,py))            

print("Cython: {:.5f}\nPython: {:.5f}\n".format(totalcy,totalpy))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))

