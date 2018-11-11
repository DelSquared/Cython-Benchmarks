from cy.cysqrt import invsqrt as cinvsqrt
from py.pysqrt import invsqrt as pinvsqrt
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

print("Checking values...\n")
if (abs(cy-py)>0.01):
    print("found mismatch in values!\n")

print("Values:\ncy: {} py:{}\n".format(cy,py))
        
            

print("Cython: {:.5f}\nPython: {:.5f}\n".format(totalcy,totalpy))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))

