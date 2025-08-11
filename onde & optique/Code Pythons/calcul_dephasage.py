# Paramètres fixes déphasage entre deux points 
A = 1.0
f = 2.0
T = 1/f
omega = 2*np.pi*f
c = 2.0
lambd = c * T
phi0 = 0

x = np.linspace(0, 3*lambd, 500)
x1 = 0.0
x2 = lambd / 4  # quart-longueur d'onde

phi_x1 = phi0 - (2 * np.pi / lambd) * x1
phi_x2 = phi0 - (2 * np.pi / lambd) * x2
dephasage = phi_x2 - phi_x1

print(f"Phase en x1={x1} m : {phi_x1:.2f} rad")
print(f"Phase en x2={x2:.2f} m : {phi_x2:.2f} rad")
print(f"Déphasage entre x1 et x2 : {dephasage:.2f} rad")

# Vérification du signe d'opposition de phase (π rad)
if np.isclose(np.abs(dephasage), np.pi, atol=1e-2):
    print("x1 et x2 vibrent en opposition de phase.")
else:
    print("x1 et x2 ne sont pas en opposition de phase.")
