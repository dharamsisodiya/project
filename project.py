import scipy.integrate as integrate
import scipy.special as sp
import numpy as np
import pylab as py
from numpy import *

# this line makes the initial intensity = 1

I0 = 1

# this allows us to pick the initial conditions. the limit here is -10 to 10 but this can be changed

print('Enter a range between -10 and 10')

lb = float(input('Enter your lower bound'))

ub = float(input('Enter your upper bound'))

x = np.arange(lb, ub, 0.1)

dx = 0.01

I_arr = []

for i in x:

    I = (I0*(2*sp.j1(x)/x))**2
    I_arr.append(I)

    # opens the file for writing

    fr = open('aFile', 'w')

    # write the character I into the file

    fr.write(str(I) + '\n')
    fr.close()

print(I_arr)
print(sum(I_arr))

Integral = sum(I_arr)*dx

yI_arr = []

y = np.arange(-10, 10, 0.1)

for j in y:

    yI = (I0*(2*sp.j1(y)/y))**2
    yI_arr.append(yI)

totIntegral = sum(yI_arr)*dx

# sum of I_arr = 2606.22 ... using lower bound as 0.01 and upper bound as 15
# gives us max of I_arr which is 0.99... but the sum of I_arr should not give 1.00 or close error
# in sum have to check sciview for error to see the array in more detail.

# stripwidth we want to be small

print(Integral/totIntegral)


# plotting

py.xlim((-20, 20))
py.ylim((-0.05, 1.1))

py.plot(x, I)
py.show()
