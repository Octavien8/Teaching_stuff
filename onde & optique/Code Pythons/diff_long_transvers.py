#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq


### Paramètres de l'onde mécanique
A = 0.3
L = 2 * np.pi
k = 2 * np.pi / L
c = 1.0
omega = k * c

x = np.linspace(0, L, 80)        ### pour onde transversale (corde)
x_long = np.linspace(0, L, 50)   ### pour onde longitudinale (son)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

### === Onde transversale (corde vibrante) ===
ax1.set_title("Onde transversale (corde vibrante)")
ax1.set_xlim(x.min(), x.max())
ax1.set_ylim(-0.5, 0.5)
ax1.set_ylabel("Déplacement vertical")
ax1.grid(True, linestyle=':')
line_trans, = ax1.plot([], [], 'b-', lw=2)
dots_trans, = ax1.plot([], [], 'bo', markersize=5)

### === Onde longitudinale (onde sonore) ===
ax2.set_title("Onde longitudinale (compression/dilatation)")
ax2.set_xlim(x_long.min() - 0.2, x_long.max() + 0.2)
ax2.set_ylim(-0.1, 0.1)
ax2.set_yticks([])
ax2.set_xlabel("Position")
ax2.grid(True, linestyle=':')
dots_long, = ax2.plot([], [], 'ro', markersize=6)

### === Initialisation ===
def init():
    line_trans.set_data([], [])
    dots_trans.set_data([], [])
    dots_long.set_data([], [])
    return line_trans, dots_trans, dots_long

### === Animation ===
def update(frame):
    t = frame / 30.0

    ### Onde transversale : y = A sin(kx - ωt)
    y_trans = A * np.sin(k * x - omega * t)
    line_trans.set_data(x, y_trans)
    dots_trans.set_data(x, y_trans)

    ### Onde longitudinale : x perturbé, y constant
    dx = A * np.sin(k * x_long - omega * t)
    x_deformed = x_long + dx
    y_line = np.zeros_like(x_long)
    dots_long.set_data(x_deformed, y_line)

    return line_trans, dots_trans, dots_long

ani = animation.FuncAnimation(fig, update, frames=240, init_func=init,
                              interval=33, blit=True)
ani.save("Cours_numeriques\\Onde_et_optique\\images\\onde_transverse-longitudinale.gif", writer=PillowWriter(fps=20))
HTML(ani.to_jshtml())
