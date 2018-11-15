from cy.cyfact import fact as cf
from py.pyfact import fact as pf
import time

a = 50000

print("Starting Cy...\n")
t0 = time.time()
for i in range(100):
    cy = cf(a)
t1 = time.time()

totalcy = t1-t0

print("Starting Py...\n")
t0 = time.time()
for i in range(100):
    py = pf(a)
t1 = time.time()

totalpy = t1-t0

print("Checking values...\n")
if (cy!=py):
    print("found mismatch in values!\n")

#print("Values:\ncy: {}\n\npy: {}\n".format(cy,py))
        
            

print("Cython: {:.5f}\nPython: {:.5f}\n".format(totalcy,totalpy))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))

