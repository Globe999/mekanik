#HUR XI VARIERAR MED TIDEN. KOLLA OLIKA BEGYNNELSEVILLKOR. Dxi/Dt


from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import math as m

# f(xi(t)) = sin^2(xi(t))
# Begynelsevilkor (0.5,0)
# W_0 = 3
# time = 10

def f(t,xi):
	return m.pow(m.sin(xi), 2)


def biss(xi):
	return 0

# def f(t, xi):
# 	w0=3
# 	g=9.81
# 	xi_prim=np.zeros(0)
# 	xi_prim = 2*xi
# 	return xi_prim


#initial vid tiden 0
y0 = [0.5]

#stop time
tend=10

# solve ODE
sol = solve_ivp(f, [0,tend], y0, method="Radau", t_eval=np.linspace(0,tend,10000))

#plot results
plt.plot(sol.t,sol.y[0,:])
plt.xlabel("time")
plt.ylabel("eta(t)")
plt.show()




def main():
	print("Hello World!")



main()
