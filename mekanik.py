#HUR XI VARIERAR MED TIDEN. KOLLA OLIKA BEGYNNELSEVILLKOR. Dxi/Dt

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import math as m


useDummy = True
a = 9
b = 1
xi0 = np.array([0.5]) #Startplats för xi
w0 = 3 #Rad per sekund
g = 9.81 #Gravitation


#DUMMY
y0 = np.array([0.5])
def dummyPrim(t, xi):
	return np.array([m.pow(m.sin(xi),2)])

def dummy2(t, xi):
	return None


#REAL VALUES


def f(t,xi):
	return a * m.pow(m.sin(xi), 2)+ b*m.pow(xi, 2)

def prim(t, xi):
	return 2*a*m.sin(xi)*m.cos(xi)+2*b

def biss(xi):
	return 2*(a*m.pow(m.cos(xi), 2)-a*m.pow(m.sin(xi),2)+b)

#initial vid tiden 0
#stop time
timeSpan = np.array([0, 10])
tend = 10


# solve ODE
#solve_ivp(<fn name>, <timespan[]>, <y0>)
sol = None
if useDummy:
	sol = solve_ivp(dummyPrim, timeSpan, y0, method="Radau", t_eval=np.linspace(0,tend,10000))
else:
	sol = solve_ivp(prim, timeSpan, xi0, t_eval=np.linspace(0,tend,10000))
print(sol)
#plot results
plt.plot(sol.t,sol.y[0,:])
plt.xlabel("time")
plt.ylabel("eta(t)")
plt.show()
