import numpy as np 
import matplotlib.pyplot as plt
from algorithms import *

def funct(x):
    """
    This is the function which we are approximating (E.G The Runge Function)
    """
    #return(np.log(1.001-np.abs(x)))
    #return(np.log(1.010-np.abs(x)))
    return(1/(1+25*x**2))
    #return(np.sin(x))


# 1. set up an array to be our 'x'
x=np.linspace(-1,1,1000)
# 2. calculate the target function f(x)
f=funct(x)

# 3. Use the function chebyApprox to calculate the 10th order approximation to f(x)
F10=chebyApprox(funct,x,order=10)

# 4. Plot the target function and the approximant and view the result, and save the figure with some name
plt.plot(x,f,label="target function")
plt.plot(x,F10,label="n=10 approximant")
plt.legend()
plt.savefig("runge_order10.png")
plt.show()

