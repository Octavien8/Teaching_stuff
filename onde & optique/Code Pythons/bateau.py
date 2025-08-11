#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq


### Paramètres de l'onde
A = 0.5          ### amplitude
L = 2.0          ### longueur d'onde
k = 2 * np.pi / L
c = 1.0          ### vitesse de propagation
omega = k * c
x = np.linspace(0, 6, 400)

### Position du bateau
x0 = 3.0
boat_width = 0.25
boat_height = 0.12

### Fonction pour créer un patch "bateau"
def make_boat_patch(xc, yc):
    half_w = boat_width/2
    pts = np.array([
        [xc - half_w, yc - boat_height*0.1],
        [xc + half_w, yc - boat_height*0.1],
        [xc,          yc + boat_height*0.9]
    ])
    return Polygon(pts, closed=True, color='brown')

### Création de la figure
fig, ax = plt.subplots(figsize=(8,3.5))
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Onde sinusoïdale → Bateau : transport d'énergie sans transport de matière")
ax.grid(True, linestyle=':', linewidth=0.5)

### Courbe de l'onde
(line,) = ax.plot([], [], lw=2, color='blue')

### Bateau
boat_patch = make_boat_patch(x0, 0)
ax.add_patch(boat_patch)

### Animation
def init():
    line.set_data([], [])
    boat_patch.set_xy(make_boat_patch(x0, 0).get_xy())
    return line, boat_patch

def update(frame):
    t = frame / 30  ### temps (s)
    y = A * np.sin(k * (x - c * t))
    line.set_data(x, y)

    ### mouvement vertical du bateau
    boat_y = A * np.sin(k * (x0 - c * t))
    boat_patch.set_xy(make_boat_patch(x0, boat_y).get_xy())
    return line, boat_patch

ani = animation.FuncAnimation(fig, update, frames=300, init_func=init,
                              blit=True, interval=33)

#ani.save("Cours_numeriques\\Onde_et_optique\\images\\bateau.gif", writer=PillowWriter(fps=20))
HTML(ani.to_jshtml())
