import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,100,100)
y = np.linspace(0,100,100)

x2 = np.linspace(0,200,100)

plt.plot(x,y)
plt.plot(x2,y)
plt.show()