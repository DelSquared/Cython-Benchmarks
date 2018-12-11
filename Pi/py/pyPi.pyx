from random import random

cpdef Pi(n):
   c=0
   for i in range(n):
      x = random()
      y = random()
      if x*x+y*y<1:
         c+=1
   return 4*c/n