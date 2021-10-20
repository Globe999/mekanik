

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import math as m

#Våra värden
a = 9
b = 1
xi0 = np.array([0.5,0]) #Begynnelsevärden
w0 = 3	#Rad per sekund
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
w0=12.8
sol2 = solve_ivp(func, timeSpan, [0.5,0], method="Radau", t_eval=np.linspace(0,timeSpan[1],10000))	
w0=13
sol3 = solve_ivp(func, timeSpan, [0.5,0], method="Radau", t_eval=np.linspace(0,timeSpan[1],10000))	
# sol2 = solve_ivp(biss, timeSpan, xi0, method="Radau", t_eval=np.linspace(0,tend,10000)
#plot results
fig,(ax1,ax2,ax3) = plt.subplots(3)
fig.suptitle("Xi(biss) vid w0=3 samt w0=13")
ax1.plot(sol.t,sol.y[0,:])
ax1.set_title("Omega = 3")
# ax1.xlabel("Time")
# ax1.ylabel("Eta(t)")

ax2.plot(sol2.t,sol2.y[0,:])
ax2.set_title("Omega = 12.8")
ax3.plot(sol3.t,sol3.y[0,:])
ax3.set_title("Omega = 13")
# ax2.xlabel("Time")
# ax2.ylabel("Eta(t)")

plt.show()
