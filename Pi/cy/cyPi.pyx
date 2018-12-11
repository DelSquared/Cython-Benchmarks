from libc.stdlib cimport rand
from libc.stdlib cimport RAND_MAX
from cython.parallel import prange

cpdef double Pi(int n):
   cdef int c=0
   cdef int i
   cdef float x
   cdef float y
   for i in prange(n, nogil=True):
      x = rand()/RAND_MAX
      y = rand()/RAND_MAX
      if x*x+y*y<1:
         c+=1
   return 4*<double>c/<double>n