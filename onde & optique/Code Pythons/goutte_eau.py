#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq


### Onde 2D : Onde à la surface de l'eau
size = 100
x = np.linspace(-10, 10, size)
y = np.linspace(-10, 10, size)
X, Y = np.meshgrid(x, y)
k = 2
omega = 3

fig, ax = plt.subplots()
c = ax.imshow(np.zeros((size, size)), extent=(-10,10,-10,10), cmap='viridis', vmin=-1, vmax=1)
ax.set_title("Onde 2D à la surface de l'eau")

def animate(t):
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(k*R - omega*t)
    c.set_array(Z)
    return c,

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 4*np.pi, 200), interval=20)
#ani.save("Cours_numeriques\\Onde_et_optique\\images\\goutte_eau.gif", writer=PillowWriter(fps=20))
HTML(ani.to_jshtml())
