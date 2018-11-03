import numpy as np
from cython.parallel import prange

cpdef Multiply(a,b):
   cdef c=np.zeros(a.shape)
   cdef int i
   cdef int j
   cdef int k
   cdef int N = a.shape[0]
   for i in prange(N, nogil=True):
      for j in prange(N):
         with gil:
            for k in range(N):
               c[i][j] = a[i][k]*b[k][j]
            
   return c