from cython.parallel import prange

cpdef fact(int x):
    y=1
    cdef int i
    for i in range(x-1):
        y *= (i+2)
    return y