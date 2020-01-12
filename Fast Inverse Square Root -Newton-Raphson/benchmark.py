from cy.cysqrt import invsqrt as cinvsqrt
from py.pysqrt import invsqrt as pinvsqrt
from math import sqrt
import time

a = 100

print("Starting Cy...\n")
t0 = time.time()
for i in range(10000000):
    cy = cinvsqrt(a)
t1 = time.time()

totalcy = t1-t0

print("Starting Py...\n")
t0 = time.time()
for i in range(10000000):
    py = pinvsqrt(a)
t1 = time.time()

totalpy = t1-t0

print("Starting Py(native)...\n")
t0 = time.time()
for i in range(10000000):
    pyn = 1/sqrt(a)
t1 = time.time()

totalpyn = t1-t0

print("Checking values...\n")
if (abs(cy-py)>0.01) or (abs(cy-pyn)>0.01):
    print("found mismatch in values!\n")

print("Values:\ncy: {} py:{} py(native):{}\n".format(cy,py,pyn))
        
            

print("Cython: {:.5f}\nPython: {:.5f}\nPython(native): {}\n".format(totalcy,totalpy,totalpyn))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))
print("Cython is {:.4f}x faster than Python(native)".format(totalpyn/totalcy))

