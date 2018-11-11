#unfortunately there was no way around using ctypes as pure Python does not permit pointers
#this code was inspired by https://github.com/ajcr/ajcr.github.io/blob/master/_posts/2016-04-01-fast-inverse-square-root-python.md

from ctypes import c_float, c_int32, cast, byref, POINTER
def invsqrt(x):
    x2 = x * 0.5
    y = c_float(x)

    i = cast(byref(y), POINTER(c_int32)).contents.value
    i = c_int32(0x5f3759df - (i >> 1))
    y = cast(byref(i), POINTER(c_float)).contents.value

    for k in range(1000):
        y  = y * ( 1.5 - ( x2 * y * y ) )
    return y
