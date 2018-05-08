import numpy as np
import matplotlib.pyplot as plt

#CONSTANTES
G = 6.674*10**(-11)
m_sol = 1.989*10**(30)
au = 149597870700
day = float(24*60*60)

#DATOS
x_mercurio =np.array([2.133679072387218e-01, -3.727310311768299e-01,-5.058864779204983e-02])*au
v_mercurio = np.array([1.892057222101034e-02, 1.513838055059527e-02, -4.995475648824679e-04])*au/day

x_tierra = np.array([-6.857609665891080e-01, -7.327391341104329e-01, -6.644615610967885e-05])*au
v_tierra = np.array([1.231562236067741e-02, -1.177303988314858e-02, 1.210619824052227e-06])*au/day

x_jupiter = np.array([-3.616450082845184e+00, -4.014244339308792e+00, 9.754215806840760e-02])*au
v_jupiter = np.array([5.517283470150529e-03, -4.691963322519999e-03, -1.039452586609281e-04])*au/day

mercurio = np.asarray([x_mercurio, v_mercurio])
tierra = np.asarray([x_tierra, v_tierra])
jupiter = np.asarray([x_jupiter, v_jupiter])

r_mag = sum(mercurio[0,:]**2)
v_mag = sum(mercurio[1,:]**2)


prob = []
x = np.linspace(0.1,4,1000)
for i in x:
    prob.append(G*m_sol*r_mag**(1-i)/v_mag**2)

plt.plot(x,prob)
plt.show()





