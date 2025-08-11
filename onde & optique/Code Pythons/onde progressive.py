#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq

#### Visualisation
x = np.linspace(0, 4*np.pi, 1000)
t = np.linspace(0, 2*np.pi, 200)
c = 1
T = 2*np.pi
lambda_ = c * T

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Onde progressive (double périodicité)")
ax.set_xlabel("Temps [s]")
ax.set_ylabel("Position [m]")

X, T_grid = np.meshgrid(x, t)
U = np.cos(2*np.pi/T_grid * T_grid - 2*np.pi/lambda_ * X)


def init():
    line.set_data([], [])
    return line,

def animate(i):
    u = np.cos(2*np.pi/T * t[i] - 2*np.pi/lambda_ * x)
    line.set_data(x, u)
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=50, blit=True)
#ani.save("Cours_numeriques\\Onde_et_optique\\images\\double_periodicite.gif", writer=PillowWriter(fps=20))
HTML(ani.to_jshtml())
