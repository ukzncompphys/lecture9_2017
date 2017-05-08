#simple_advect_finite_volume.py
import numpy
from matplotlib import pyplot as plt
import time

n=300
#rho=numpy.zeros(n)
#rho[n/3:(2*n/3)]=1
#x=numpy.arange(n)*dx

x=numpy.arange(n);x=x-0.5*n
rho=numpy.exp(-0.5*(x/20)**2)


v=1.0
dx=1.0


plt.ion()
plt.clf()
#plt.axis([0,n,0,1.1])
plt.plot(x,rho)
plt.draw()
plt.savefig('advect_initial_conditions.png')

dt=1.0
for step in range(0,50):
    time.sleep(0.2)
    #take the difference in densities
    drho=rho[1:]-rho[0:-1]
    #update density.  We haven't said what happens at
    #cell 0 (since cell -1 doesn't exist), ignore for now
    rho[1:]=rho[1:]-v*dt/dx*drho
    plt.clf()
    #plt.axis([0,n,0,1.1])
    plt.plot(x,rho)
    plt.draw()

