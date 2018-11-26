from cy.cyroot import root as croot
from py.pyroot import root as proot
import time

dx=0.0001
n=100000000

def f(x):
    return x*x

print("Finding roots of f(x)=x^2 for {} iterations with {} step size\n".format(n,dx))

print("Starting Cy...\n")
t0 = time.time()
for i in range(5):
    cy = croot(f,dx,n)
t1 = time.time()

totalcy = t1-t0

print("Starting Py...\n")
t0 = time.time()
for i in range(5):
    py = proot(f,dx,n)
t1 = time.time()

totalpy = t1-t0

print("Checking values...\n")
if (abs(cy-py)>0.1):
    print("found mismatch in values!\n")

print("Values:\ncy: {} py: {}\n".format(cy,py))
        
            

print("Cython: {:.5f}\nPython: {:.5f}\n".format(totalcy,totalpy))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))

