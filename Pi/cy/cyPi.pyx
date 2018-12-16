from libc.stdlib cimport rand
from libc.stdlib cimport RAND_MAX
from cython.parallel import prange

cpdef double Pi(int n):
   cdef long c=0
   cdef long i
   cdef double x
   cdef double y
   for i in prange(n, nogil=True,num_threads=6):
      x = <double>rand()/<double>RAND_MAX
      y = <double>rand()/<double>RAND_MAX
      if (x*x+y*y)<1:
         c+=1
   return 4*<double>(c)/<double>n
