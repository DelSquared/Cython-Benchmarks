cdef extern from *:
    """
    //Yanked from the Quake III Arena source code as provided on the Wikipedia article
    float c_invsqrt( float number ){
        long i;
        float x2, y;

        x2 = number * 0.5F;
        y  = number;
        i  = * ( long * ) &y;
        i  = 0x5f3759df - ( i >> 1 );
        y  = * ( float * ) &i;
        y  = y * (1.5F - ( x2 * y * y ) );
        return y;
    }

    """
    float c_invsqrt(float number)


cpdef float invsqrt(float number):
    return c_invsqrt(number)
