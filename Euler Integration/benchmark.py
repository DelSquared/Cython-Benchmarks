from cy.cyinteg import integ as cint
from py.pyinteg import integ as pint
import time

x1=0
x2=10
n=100000000

def f(x):
    return x*x+x+1

print("Integrating function f(x)=x^2+x+1 on the interval [{},{}] with {} parts\n".format(x1,x2,n))

print("Starting Cy...\n")
t0 = time.time()
for i in range(10):
    cy = cint(f,x1,x2,n)
t1 = time.time()

totalcy = t1-t0

print("Starting Py...\n")
t0 = time.time()
for i in range(10):
    py = pint(f,x1,x2,n)
t1 = time.time()

totalpy = t1-t0

print("Checking values...\n")
if (abs(cy-py)>0.1):
    print("found mismatch in values!\n")

print("Values:\ncy: {}\n\npy: {}\n".format(cy,py))
        
            

print("Cython: {:.5f}\nPython: {:.5f}\n".format(totalcy,totalpy))
print("Cython is {:.4f}x faster than Python".format(totalpy/totalcy))

