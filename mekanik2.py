from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import math as m

#####################################
##          VALUES                 ##
#####################################
omega = 80
t = 1
g = 9.81
U0 = [0.0174533, 0] #Startvärden i radianer
#Meters
L=1
r1 = 0.04
r2 = 0.05
R = 0.05

#kg/m^3
p = 7800
#Vikter
v1 = (4*m.pi*m.pow(r1,3))/3
v2 = (4*m.pi*m.pow(r2,3))/3-v1
m1 = p * v1
m2 = p * v2
M = m1+m2
i2 = (2/3)*m.pow(r2,2)*m2
l = (i2 + M*m.pow((L+r2),2))/(M*(L+r2))


#####################################
##          Function               ##
#####################################
def dU_dt(U,t):
    return [U[1],-(((R*m.pow(omega,2)*m.sin(omega*t)-g)*U[0]+R*m.pow(omega, 2)*m.cos(omega*t))/l)]

xs = np.linspace(0, 100, 10000)

#####################################
##  Solve for different omgeas     ##
#####################################
sol1 = odeint(dU_dt, U0, xs)
omega = 90
sol2 = odeint(dU_dt, U0, xs)
omega = 95
sol3 = odeint(dU_dt, U0, xs)
omega = 100
maxval = np.max(sol3[:,0])
sol4 = odeint(dU_dt, U0, xs)
omega = 130
sol5 = odeint(dU_dt, U0, xs)
omega = 1000
sol6 = odeint(dU_dt, U0, xs)


print(maxval)

#####################################
##            Plot                 ##
#####################################

fig, axs = plt.subplots(3,2,sharex=True)

fig.suptitle("Omega at 80, 90, 95, 100, 130 & 1000")
#plot graphs
axs[0,0].plot(xs,sol1[:,0])
axs[0,0].set_title("Omega = 80")

axs[0,1].plot(xs,sol2[:,0])
axs[0,1].set_title("Omega = 90")

axs[1,0].plot(xs,sol3[:,0])
axs[1,0].set_title("Omega = 95")

axs[1,1].plot(xs,sol4[:,0])
axs[1,1].set_title("Omega = 100")

axs[2,0].plot(xs,sol5[:,0])
axs[2,0].set_title("Omega = 130")

axs[2,1].plot(xs,sol6[:,0])
axs[2,1].set_title("Omega = 1000")

fig.add_subplot(111, frame_on=False)
plt.tick_params(labelcolor="none", bottom=False, left=False)

plt.xlabel("Time [s]")
plt.ylabel("Phi [rad]")

plt.show()