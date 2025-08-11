#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq



### Paramètres fixes
S1, S2 = 1.0, 1.0          ### Amplitudes
omega = 2 * np.pi          ### Pulsation (1 Hz)
t = np.linspace(0, 2, 1000)

def plot_sinusoids(phi1=0.0, phi2=np.pi/3):
    s1 = S1 * np.cos(omega * t + phi1)
    s2 = S2 * np.cos(omega * t + phi2)
    s = s1 + s2

    plt.figure(figsize=(10, 5))
    plt.plot(t, s1, label='Signal s1')
    plt.plot(t, s2, label='Signal s2')
    plt.plot(t, s, label='Somme s1 + s2', linewidth=2)
    plt.title('Addition de deux signaux sinusoïdaux')
    plt.xlabel('Temps (s)')
    plt.ylabel('Amplitude')
    plt.ylim(- (S1 + S2 + 0.2), S1 + S2 + 0.2)
    plt.legend()
    plt.grid(True)
    plt.show()

### Curseurs interactifs pour phi1 et phi2 en radians de 0 à 2pi
interact(plot_sinusoids,
         phi1=FloatSlider(min=0, max=np.pi, step=0.01, value=0, description=r'$\phi_1$'),
         phi2=FloatSlider(min=0, max=np.pi, step=0.01, value=np.pi/3, description=r'$\phi_2$'));
