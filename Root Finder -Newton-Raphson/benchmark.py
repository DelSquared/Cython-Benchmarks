from cy.cyroot import root as croot
from py.pyroot import root as proot
import time

dx=1
n=100000000

def f(x,der=False):
    if der==False:
        return x*x-2
    else:
        return 2*x

print("Finding roots of f(x)=x^2-2 for {} iterations with {} step size\n".format(n,dx))

print("Starting Cy...\n")
t0 = time.time()
for i in range(3):
    cy = croot(f,dx,n)
t1 = time.time()

totalcy = t1-t0

print("Starting Py...\n")
t0 = time.time()
for i in range(3):
    py = proot(f,dx,n)
t1 = time.time()

totalpy = t1-t0

print("Checking values...\n")
if (abs(cy-py)>0.01):
    print("found mismatch in values!\n")

print("Values:\ncy: {}\n\npy: {}\n".format(cy,py))
        
            

print("Cython: {:.5f}\nPython: {:.5f}\n".format(totalcy,totalpy))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))

