def root(func,dx,iter):
    x=10
    for i in range(iter):
        x  -= func(x)*dx
    return x
