
#### Lib Python (Version > 3.0)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from IPython.display import HTML
from ipywidgets import interact, FloatSlider

from scipy.fft import fft, fftfreq
#### 3. Exemple : signaux sonores


### Paramètres
f1, f2 = 50, 250  ### fréquences en Hz
A1, A2 = 1.0, 0.5  ### amplitudes respectives
fs = 6000  ### fréquence d'échantillonnage (Hz)
T = 0.2  ### durée du signal (s)
t = np.linspace(0, T, int(fs*T), endpoint=False)

### Signal dans le domaine temporel
signal = A1 * np.sin(2*np.pi*f1*t) + A2 * np.sin(2*np.pi*f2*t)

### FFT
Y = fft(signal)
freqs = fftfreq(len(t), d=1/fs)

### Affichage
plt.figure(figsize=(12, 5))

### Domaine temporel
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.xlim(0, .1)
plt.title("Signal temporel")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")

### Domaine fréquentiel
plt.subplot(1, 2, 2)
plt.plot(freqs[:len(freqs)//2], np.abs(Y[:len(Y)//2]) / len(t))

plt.title("Spectre de Fourier (amplitude)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
#plt.savefig("Cours_numeriques\\Onde_et_optique\\images\\signal_sonore_fourier.png")
plt.show()
