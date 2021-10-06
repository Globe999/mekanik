#HUR XI VARIERAR MED TIDEN. KOLLA OLIKA BEGYNNELSEVILLKOR. Dxi/Dt

from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt
import numpy as np
import math as m

omega = 10
t = 1
g = 9.81 #Gravitation
u0 = np.array([1,1])
#Längder
L=2
r1 = 1
r2 = 1
R = 1
#Vikter
m1 = 10
m2 = 20
M = m1+m2


i2 = (2/3)*m.pow(r2,2)*m2

l = (i2 + M*m.pow((L+r2),2))/(M*(L+r2))

def dU_dx(U,t):
    return [U[1], -(((R*m.pow(omega,2)*m.sin(omega*t)-g)*U[0]+R*m.pow(omega, 2)*m.cos(omega*t))/l)]

U0 = [0, 0]
xs = np.linspace(0, 100, 200)
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]


plt.xlabel("x")
plt.ylabel("y")
plt.title("Pendeljävel")
plt.plot(xs,ys);
plt.show()


#initial vid tiden 0
#stop time
# timeSpan = np.array([0, 100])
# tend = 10


# # solve ODE
# #solve_ivp(<fn name>, <timespan[]>, <y0>)
# sol = None

# sol = solve_ivp(f, timeSpan, fi0, t_eval=np.linspace(0,tend,10000))
# print(sol)
# #plot results
# plt.plot(sol.t,sol.y[0,:])
# plt.xlabel("time")
# plt.ylabel("eta(t)")
# plt.show()
