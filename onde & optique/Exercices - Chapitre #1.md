## Exercices
#### 1D — Onde unidimensionnelle

##### Exercice 1
**Énoncé** Sur une corde infinie, l'onde $u(x,t) = A \sin(kx - \omega t)$ est donnée, avec $A=1$, $k=2\pi$, $\omega = 4\pi$.
- Vérifier qu'elle satisfait l'équation d'onde 1D : $u_{tt} = c^2 u_{xx}$.
- Déterminer la célérité $c$.

**Correction** 1.  On calcule la dérivée partielle de $u$ par rapport au temps ($u_{tt}$) : 
    $$u_t = \frac{\partial u}{\partial t} = A(-\omega)\cos(kx - \omega t)$$   
    $$u_{tt} = \frac{\partial^2 u}{\partial t^2} = A(-\omega)^2(-\sin(kx - \omega t)) = -A\omega^2\sin(kx - \omega t)$$

2.  On calcule la dérivée partielle de $u$ par rapport à l'espace ($u_{xx}$) :
    $$u_x = \frac{\partial u}{\partial x} = A(k)\cos(kx - \omega t)$$   
    $$u_{xx} = \frac{\partial^2 u}{\partial x^2} = A(k)^2(-\sin(kx - \omega t)) = -Ak^2\sin(kx - \omega t)$$

3.  On injecte les résultats dans l'équation d'onde :
    $$u_{tt} = c^2 u_{xx}$$   
    $$-A\omega^2\sin(kx - \omega t) = c^2(-Ak^2\sin(kx - \omega t))$$
    En simplifiant par $-A\sin(kx - \omega t)$, on obtient :
    $$\omega^2 = c^2 k^2 \implies c = \frac{\omega}{k}$$

4.  On calcule la valeur de $c$ avec les données de l'énoncé :
    $$c = \frac{4\pi}{2\pi} = 2$$
    La célérité de l'onde est donc $c=2$ (en unités de distance par unité de temps).

---

##### Exercice 2
**Énoncé** Décomposer la solution générale de l'équation d'onde 1D :
$$\frac{\partial^2 u}{\partial t^2} = 9 \frac{\partial^2 u}{\partial x^2}$$
en ondes progressives et déterminer la célérité $c$.

**Correction** L'équation donnée est de la forme $u_{tt} = c^2 u_{xx}$.
En comparant les deux équations, on identifie $c^2 = 9$, ce qui donne $c=3$.

La solution générale de l'équation d'onde 1D peut être décomposée en deux ondes progressives, selon le principe de d'Alembert :
$$u(x, t) = f(x - ct) + g(x + ct)$$
Ici, la solution générale est donc :
$$u(x, t) = f(x - 3t) + g(x + 3t)$$
où $f$ représente une onde se propageant vers la droite et $g$ une onde se propageant vers la gauche, toutes deux à la célérité $c=3$.

---

##### Exercice 3
**Énoncé** Sur une corde infinie, les conditions initiales sont :
$$u(x,0) = 0, \quad \frac{\partial u}{\partial t}(x,0) = v(x) = \begin{cases}
1, & 0 \le x \le 1 \\
0, & \text{sinon}
\end{cases}$$
et la célérité de l'onde est $c = 1$. Trouver $u(x, t)$.

**Correction** La solution de l'équation d'onde 1D pour une corde infinie, avec une position initiale nulle ($u(x,0)=0$), est donnée par la formule de d'Alembert :

$$u(x,t) = \frac{1}{2c} \int_{x-ct}^{x+ct} v(\xi) d\xi$$
Avec $c=1$, on obtient :
$$u(x,t) = \frac{1}{2} \int_{x-t}^{x+t} v(\xi) d\xi$$
L'intégrale représente la surface sous la fonction $v(\xi)$, qui est un créneau de hauteur 1 et de largeur 1 sur l'intervalle $[0, 1]$. La solution $u(x,t)$ représente l'onde qui se divise en deux parties et se propage vers la droite et la gauche à partir de la perturbation initiale.

**Calcul explicite de l'intégrale (pour c = 1):**

L'intégrale représente l'aire sous la fonction v(ξ) (créneau unitaire sur [0,1]) 
entre x-t et x+t.

Pour calculer cette intégrale, il faut considérer l'intersection entre 
l'intervalle d'intégration [x-t, x+t] et le support de v(ξ) qui est [0,1] :

Intersection = [x-t, x+t] ∩ [0,1] = [max(0, x-t), min(1, x+t)]

**Cas différents :**

1. **Si x+t < 0 ou x-t > 1** : Pas d'intersection → u(x,t) = 0

2. **Si 0 ≤ x-t et x+t ≤ 1** : L'intervalle [x-t, x+t] est entièrement dans [0,1]
   $$u(x,t) = \frac{1}{2} \int_{x-t}^{x+t} d\xi = \frac{1}{2} × 2t = t$$

3. **Cas partiels** : L'intersection est [max(0, x-t), min(1, x+t)]
   $$u(x,t) = \frac{1}{2}[min(1, x+t) - max(0, x-t)]$$

**Expression générale :**

$$u(x,t) = \frac{1}{2} × max(0, min(1, x+t) - max(0, x-t))$$

**Interprétation physique :**

La solution représente la superposition de deux demi-créneaux :
- Un demi-créneau d'amplitude 1/2 se propageant vers la droite
- Un demi-créneau d'amplitude 1/2 se propageant vers la gauche

Chaque demi-créneau a une largeur unitaire et ils s'éloignent l'un de l'autre 
à la vitesse c = 1.

---

#### 2D — Onde bidimensionnelle

###### Exercice 4
**Énoncé** Pour l'EDP en 2D :
$$u_{tt} = c^2 (u_{xx} + u_{yy})$$
expliquer pourquoi l'amplitude d'une onde plane se propageant dans cette équation ne décroît pas avec la distance.

**Correction** Une onde plane 2D est caractérisée par des fronts d'onde parallèles. L'énergie de l'onde est transportée le long de ces fronts sans se disperser sur une surface plus grande. L'intensité de l'onde (énergie par unité de temps et par unité de longueur du front d'onde) reste constante. Puisque l'intensité est proportionnelle au carré de l'amplitude ($I \propto A^2$), l'amplitude de l'onde ne décroît pas avec la distance.

---

##### Exercice 5
**Énoncé** Une source ponctuelle à l'origine produit une onde circulaire dans l'eau. Montrer que l'amplitude à distance $r$ décroît comme $1/\sqrt{r}$.

**Correction** Dans ce cas, l'énergie de la source ponctuelle se propage de manière isotrope, c'est-à-dire dans toutes les directions. En 2D, cette énergie est distribuée sur une circonférence de rayon $r$.
- La **puissance** totale ($P$) de la source est constante.
- L'**intensité** de l'onde ($I$), qui est la puissance par unité de longueur du front d'onde, est donnée par $I = \frac{P}{2\pi r}$.
- L'**amplitude** de l'onde ($A$) est proportionnelle à la racine carrée de l'intensité ($A \propto \sqrt{I}$).
En combinant ces relations, on obtient :
$$A \propto \sqrt{\frac{P}{2\pi r}} \implies A \propto \frac{1}{\sqrt{r}}$$
L'amplitude de l'onde décroît donc comme $1/\sqrt{r}$.

---

##### Exercice 6
**Énoncé** Une membrane circulaire de rayon $R$ est frappée en son centre. La perturbation se propage en cercles. Expliquer qualitativement la solution via les fonctions de Bessel (ordre 0) et pourquoi elle décroît avec $r$.

**1. Forme de la solution :**

Pour une membrane circulaire avec symétrie radiale, l'équation d'onde 2D en coordonnées polaires se réduit à :
$$\frac{\partial^2 u}{\partial t^2} = c^2 \left(\frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r}\right)$$

Par séparation de variables $u(r,t) = R(r)T(t)$, on obtient pour la partie radiale :
$$r^2 R'' + r R' + k^2 r^2 R = 0$$

Cette équation de Bessel d'ordre 0 a pour solution $R(r) = A J_0(kr) + B Y_0(kr)$.

**2. Conditions aux limites :**

- Pour éviter la divergence en $r=0$, on doit avoir $B=0$ (car $Y_0(0) \to -\infty$)
- À la frontière $r=R$, condition aux limites (par exemple $u(R,t)=0$) → $J_0(kR)=0$

La solution s'écrit donc : $u(r,t) = \sum_n A_n J_0(k_n r) \cos(\omega_n t + \phi_n)$

**3. Décroissance avec $r$ :**

La décroissance provient de deux effets :

**a) Comportement asymptotique de $J_0$ :**
Pour $kr \gg 1$ :
$$J_0(kr) \sim \sqrt{\frac{2}{\pi kr}} \cos\left(kr - \frac{\pi}{4}\right)$$

Donc $J_0(kr) \propto \frac{1}{\sqrt{r}}$ pour les grandes valeurs de $r$.

**b) Conservation de l'énergie :**
L'énergie se répartit sur des cercles de circonférence croissante $2\pi r$. Par conservation de l'énergie, l'intensité (énergie par unité de longueur) décroît comme $1/r$, donc l'amplitude décroît comme $1/\sqrt{r}$.

**Conclusion :** La fonction de Bessel $J_0$ modélise naturellement cette décroissance géométrique de l'amplitude avec la distance, combinée à son comportement oscillant caractéristique des ondes stationnaires dans un domaine borné.

---

#### 3D — Onde tridimensionnelle

##### Exercice 7
**Énoncé** Vérifier que la fonction sphérique :
$$u(r, t) = \frac{1}{r} f(r - ct)$$
est solution de l'EDP en 3D :
$$u_{tt} = c^2 \Delta u$$
pour $r \neq 0$.

**Correction** En coordonnées sphériques, le laplacien d'une fonction à symétrie radiale, $u(r,t)$, est donné par :
$$\Delta u = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial u}{\partial r} \right) = \frac{\partial^2 u}{\partial r^2} + \frac{2}{r} \frac{\partial u}{\partial r}$$
Pour simplifier la vérification, on peut poser $v(r,t) = ru(r,t)$. On a donc $u = v/r$.
L'équation d'onde 3D devient alors :
$$\frac{1}{r} \frac{\partial^2 v}{\partial t^2} = c^2 \left( \frac{1}{r} \frac{\partial^2 v}{\partial r^2} \right)$$
$$v_{tt} = c^2 v_{rr}$$
C'est l'équation d'onde 1D pour la fonction $v$. Or, la fonction $v(r,t) = r u(r,t) = f(r-ct)$ est bien une solution de cette équation 1D. Par conséquent, $u(r,t) = \frac{1}{r} f(r-ct)$ est une solution de l'équation d'onde 3D.

---

##### Exercice 8
**Énoncé** Une onde sonore se propage à partir d'une source ponctuelle dans l'air. Justifier que la pression acoustique moyenne diminue comme $1/r$.

**Correction** Dans un espace 3D, l'énergie de l'onde se disperse sur une surface sphérique de rayon $r$.
- La **puissance** de la source ($P$) est constante.
- L'**intensité** de l'onde ($I$), qui est la puissance par unité de surface, est donnée par $I = \frac{P}{4\pi r^2}$ (la surface d'une sphère est $4\pi r^2$).
- La pression acoustique ($p$) est proportionnelle à la racine carrée de l'intensité ($p \propto \sqrt{I}$).
On a donc :
$$p \propto \sqrt{\frac{P}{4\pi r^2}} \implies p \propto \frac{1}{r}$$
L'amplitude de pression acoustique diminue donc comme $1/r$.

---

##### Exercice 9
**Énoncé** Dans un contexte électromagnétique, une onde sphérique se propage dans le vide. Justifier que l'amplitude du champ électrique se comporte comme $1/r$ loin de la source.

**Correction** Ce raisonnement est identique à celui de l'exercice précédent. L'énergie rayonnée par la source électromagnétique se répartit sur une surface sphérique de rayon $r$.
- L'**intensité** de l'onde électromagnétique ($I$) est proportionnelle au carré de l'amplitude du champ électrique $E$ ($I \propto E^2$).
- L'intensité décroît avec la surface de la sphère, soit $I \propto \frac{1}{r^2}$.
- En combinant ces deux relations, on obtient $E^2 \propto \frac{1}{r^2}$, ce qui implique que l'amplitude du champ électrique $E$ décroît comme $1/r$ pour les grandes distances.
