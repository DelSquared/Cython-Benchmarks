# Cython-Benchmarks
Cython Benchmarks: I will be putting both Python and Cython versions of the same functions and comparing their speed and performance

## Matrix Multiplication Output

```
Initialising arrays with dimension 1000x1000

Starting Cy...

Starting Py...

Checking arrays...

Cython: 260.85251
Python: 416.96802

Cython is 1.5985x faster than Python
```

## Inverse Square Root (Newton-Raphson)

```
Starting Cy...

Starting Py...

Checking values...

Values:
cy: 0.10000000149011612 py:0.09999999999999999

Cython: 60.77959
Python: 305.20921

Cython is 5.0216x faster than Python
```

## Factorial

```
Starting Cy...

Starting Py...

Checking values...

Cython: 47.38556
Python: 47.46324

Cython is 1.0016x faster than Python
```
<sub>I was honestly very surprised that these were this close with only ~0.2% improvement</sub>

## Euler Integration

```
Integrating function f(x)=x^2+x+1 on the interval [0,10] with 1000000 parts

Starting Cy...

Starting Py...

Checking values...

Values:
cy: 18.34343910217285 py: 18.333323333334896

Cython: 1.15893
Python: 1.55387

Cython is 1.3408x faster than Python
```

## Root Finder (Gradient Descent hack)

```
Finding roots of f(x)=x^2 for 100000000 iterations with 0.0001 step size

Starting Cy...

Starting Py...

Checking values...

Values:
cy: 0.0005394796608015895 py: 9.999898849677766e-05

Cython: 39.02174
Python: 39.75569

Cython is 1.0188x faster than Python
```

## Root Finder (Newton-Raphson)

```
Finding roots of f(x)=x^2-2 for 100000000 iterations with 1 step size

Starting Cy...

Starting Py...

Checking values...

Values:
cy: 1.4142135381698608

py: 1.4142135623730951

Cython: 148.43348
Python: 150.23746

Cython is 1.0122x faster than Python
```
