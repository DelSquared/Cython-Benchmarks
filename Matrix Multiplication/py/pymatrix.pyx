import numpy as np

def Multiply(a,b):
   c=np.zeros(a.shape)
   for i in range(a.shape[0]):
      for j in range(a.shape[0]):
         for k in range(a.shape[0]):
            c[i][j] += a[i][k]*b[k][j]
   return c
