cpdef invsqrt(x):
    cdef int i
    cdef float x2, y

    x2 = x* 0.5
    y  = x

    i  = (<long*> &y)[0]
    i  = 0x5f3759df - ( i >> 1 )
    y  = (<float*> &i)[0]

    cdef int k
    for k in range(1000):
        y  = y * ( 1.5 - ( x2 * y * y ) )

    return y