import numpy as np
import pylab

x=np.linspace(-1,1,1000)
y=(x**2)*np.cos(1/x)
pylab.plot(x, y)