import numpy as np
import matplotlib.pyplot as plt
def log_iterate(zn,r,n):
    for i in range(n):
        zn=r*zn*(1-zn)
    return zn

converge=[]

rs=np.arange(2.9,4.,0.00001)
converge = log_iterate(np.random.uniform(0.,1.,size=rs.shape),rs,1000)

plt.figure()
plt.title("Convergence value versus Growth rate $Population(P) vs Population Growth(r)-$")
plt.plot(rs, converge,'.',markersize=0.3)

plt.show()