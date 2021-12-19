import numpy as np
import matplotlib.pyplot as plt
def log_iterate(zn,r,n):
    for i in range(n):
        zn=r*zn*(1-zn)
    return zn

converge=[]
growth=[]
cnt=0
rs=np.arange(2.9,4.,0.000001)
converge = log_iterate(np.random.uniform(0.,1.,size=rs.shape),rs,100)
print(cnt)
plt.figure()
plt.title("Convergence value versus Growth rate")
plt.plot(rs, converge,'.',markersize=0.1)

plt.show()