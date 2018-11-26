def root(func,dx,iter):
    x=1000
    for i in range(iter):
        if func(x,der=True)==0:
            break
        x  -= func(x)*dx/func(x,der=True)
    return x