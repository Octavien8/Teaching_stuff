#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq


### Onde 1D : Onde sur une corde
x = np.linspace(0, 10, 500)
k = 2 * np.pi / 5  ### nombre d'onde
omega = 2 * np.pi / 2  ### pulsation
A = 1  ### amplitude

fig, ax = plt.subplots(figsize=(10, 4))
line, = ax.plot(x, np.zeros_like(x))
ax.set_ylim(-1.2 * A, 1.2 * A)
ax.set_title("Onde 1D : Onde sur une corde")
ax.set_xlabel("Position x")
ax.set_ylabel("Déplacement")

def animate(t):
    y = A * np.sin(k * x - omega * t)
    line.set_ydata(y)
    return line,

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 4*np.pi, 200), interval=30)
ani.save("Cours_numeriques\\Onde_et_optique\\images\\corde.gif", writer=PillowWriter(fps=20))
HTML(ani.to_jshtml())
