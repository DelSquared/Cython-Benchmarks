ctypedef float (*f_type)(float)

cpdef root(func,float dx,int iter):
    cdef float x=10
    cdef int i
    for i in range(iter):
        x  -= func(x)*dx
    return x
