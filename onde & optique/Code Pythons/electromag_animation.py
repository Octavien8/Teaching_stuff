#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq

### Paramètres
k = 2 * np.pi / 4  ### nombre d'onde
omega = 2 * np.pi / 4  ### pulsation
A = 1
x = np.linspace(0, 4 * np.pi, 100)
n_vec = 20
x_vec = np.linspace(0, 4 * np.pi, n_vec)


### Création de la figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

def animate(t):
    ax.clear()
    
    E_y = A * np.sin(k * x - omega * t)
    B_z = A * np.sin(k * x - omega * t)
    E_vec = A * np.sin(k * x_vec - omega * t)
    B_vec = A * np.sin(k * x_vec - omega * t)

    for xi, Ei in zip(x_vec, E_vec):
        if abs(Ei) > 0.05:
            ax.plot([xi, xi], [0, Ei], [0, 0], 'r-', linewidth=2, alpha=0.8)

    for xi, Bi in zip(x_vec, B_vec):
        if abs(Bi) > 0.05:
            ax.plot([xi, xi], [0, 0], [0, Bi], 'b-', linewidth=2, alpha=0.8)

    ax.plot(x, E_y, np.zeros_like(x), 'r--', alpha=0.5, linewidth=1)
    ax.plot(x, np.zeros_like(x), B_z, 'b--', alpha=0.5, linewidth=1)

    ax.plot([0, 4*np.pi], [0, 0], [0, 0], 'k-', alpha=0.3)
    ax.plot([0, 0], [-1.5, 1.5], [0, 0], 'k-', alpha=0.3)
    ax.plot([0, 0], [0, 0], [-1.5, 1.5], 'k-', alpha=0.3)

    ax.text(4*np.pi + 0.2, 0, 0, 'x', fontsize=12, color='black')
    ax.text(0, 1.7, 0, 'y', fontsize=12, color='red')
    ax.text(0, 0, 1.7, 'z', fontsize=12, color='blue')
    #ax.text(np.pi, 1.3, 0, 'Champ électrique E', fontsize=10, color='red')
    #ax.text(np.pi, 0, 1.3, 'Champ magnétique B', fontsize=10, color='blue')
    #ax.text(2*np.pi, -1.5, -1.5, 'Direction de propagation →', fontsize=10, color='black')

    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-1.5, 1.5)
    ax.set_xlabel('x (direction de propagation)')
    ax.set_ylabel('Champ électrique E')
    ax.set_zlabel('Champ magnétique B')
    ax.view_init(elev=20, azim=45)
    ax.set_title('Onde électromagnétique animée\n(E en rouge, B en bleu)', fontsize=14, pad=20)

ani = FuncAnimation(fig, animate, frames=100, interval=300)
#ani.save("Cours_numeriques\\Onde_et_optique\\images\\electromag_2.gif", writer=PillowWriter(fps=20))
HTML(ani.to_jshtml())
