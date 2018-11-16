def integ(func,x1,x2,n):
    dx = abs(x2-x1)/n
    y=0
    for i in range(n):
        y  += func(x1+i/n)*dx
    return y