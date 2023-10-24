import numpy as np
import pylab

x=np.linspace(-1,1,1000)
y=(x)*np.sin(1/x)
pylab.plot(x, y)