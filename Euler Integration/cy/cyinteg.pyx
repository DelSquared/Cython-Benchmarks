ctypedef float (*f_type)(float)

cpdef integ(func,float x1,float x2,int n):
    cdef float parts =  n
    cdef float dx = abs(x2-x1)/parts 
    cdef float y=0
    cdef int i
    for i in range(n):
        y  += func(x1+(<float>i)/parts)*dx
    return y