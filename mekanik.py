#HUR XI VARIERAR MED TIDEN. KOLLA OLIKA BEGYNNELSEVILLKOR. Dxi/Dt

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import math as m


a = 9
b = 1
xi0 = np.array([0.5,0]) #Startplats för xi
w0 = 13	#Rad per sekund
g = 9.81 #Gravitation


def f(xi):
	return a * m.pow(m.sin(xi), 2)+ b*m.pow(xi, 2)

def fPrim(xi):
	return 2*a*m.sin(xi)*m.cos(xi)+2*b*xi

def fBiss(xi):
	return 2*(a*m.pow(m.cos(xi), 2)-a*m.pow(m.sin(xi),2)+b)


def func(t,xi):
	xiPrim=[0,0]
	xiPrim[0]=xi[1]
	xiPrim[1] = (m.pow(w0,2)*xi[0]-fPrim(xi[0])*fBiss(xi[0])*m.pow(xi[1],2)-fPrim(xi[0])*g)/(m.pow(fPrim(xi[0]),2)+1)
	return xiPrim

#stop time
timeSpan = np.array([0, 10])



# solve ODE
#solve_ivp(<fn name>, <timespan[]>, <y0>)

sol = solve_ivp(func, timeSpan, [0.5,0], method="Radau", t_eval=np.linspace(0,timeSpan[1],10000))
	# sol2 = solve_ivp(biss, timeSpan, xi0, method="Radau", t_eval=np.linspace(0,tend,10000))
print(sol)
#plot results
plt.plot(sol.t,sol.y[0,:])
plt.xlabel("time")
plt.ylabel("eta(t)")
plt.show()
