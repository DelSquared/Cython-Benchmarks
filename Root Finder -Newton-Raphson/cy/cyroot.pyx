ctypedef float (*f_type)(float)

cpdef root(func,float dx,int iter):
    cdef float x=1000
    cdef int i
    for i in range(iter):
        if func(x,der=True)==0:
            break
        x  -= dx*func(x)/func(x,der=True)
    return x