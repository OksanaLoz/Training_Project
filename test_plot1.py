import numpy as np
import pylab

x=np.linspace(-1,1,1000)
y=(x-x**3)*np.exp(-1/(x**2))
pylab.plot(x, y, "--g")