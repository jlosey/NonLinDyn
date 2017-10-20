import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

class diffSys:
    """Base class for system of differential equations object."""
    def __init__(self,x0):
        self.x1 = np.resize(x0,(1,len(x0))) 
        self.x2 = self.eval(x0)
    
    def add_step(self,xi):
        self.x1 = np.concatenate((self.x1,xi))
        x2i = self.eval(xi[0])
        self.x2 = np.concatenate((self.x2,x2i))

class sho(diffSys):
    """Create simple harmonic oscillator object that extends 
    diffSys"""
    def __init__(self,spring,mass,damp,x0):
        self.k = spring
        self.m = mass
        self.beta = damp
        diffSys.__init__(self,x0)
    
    def eval(self,xi):
        e = [xi[1],-(self.k/self.m)*xi[0] - xi[1]*self.beta]
        return np.resize(e,(1,2))

class lorentz(diffSys):
    """Create Lorentz eq object that extends diffSys
    to store state point trajectory"""
    def __init__(self,sig,r,b,x0):
        self.sigma = sig
        self.rho = r
        self.beta = b
        diffSys.__init__(self,x0)
    def eval(self,xi):
        xdot = self.sigma*(xi[1]-xi[0])
        ydot = xi[0]*(self.rho - xi[2])-xi[1]
        zdot = xi[0]*xi[1] - self.beta*xi[2]
        return np.asarray([[xdot,ydot,zdot]])

def forwardEuler(s,x0,tstep):
    "Advance one time step using Forward Euler ODE"
    n = x0.size
    x2 = s.eval(x0)
    x1 = x0 + tstep*x2[0]
    return np.resize(x1,(1,n))

def backwardEuler(s,x0,tstep):
    "Backward Euler algorithm for simple harmonic oscillator."
    n = x0.size
    x1f = forwardEuler(s,x0,tstep)
    x2f = s.eval(x1f[0])
    x1 = x0 + tstep*x2f
    return np.resize(x1,(1,n))

def trapezoid(s,x0,tstep):
    "Trapezoid algorithm to average forward and backward Euler steps."
    #x1f = forwardEuler(s,x0,tstep)
    n = x0.size
    x2f = s.eval(x0)
    x1b = forwardEuler(s,x0,tstep)
    x2b = s.eval(x1b[0])
    x1 = x0 + tstep*((x2f + x2b)/2)
    return np.resize(x1,(1,n))

def rk4(s,x0,tstep):
    k1 = s.eval(x0)
    x1 = xi + tstep*(k1+2*k2+2*k3+k4)/6
    return x1

x0 =[-1,-2]
step = 0.01
t = 0
tlist = [t]

k = 2
m = 0.5 
beta = 0
#initialize
#sf = sho(k,m,beta,x0)
#sb = sho(k,m,beta,x0)
st = sho(k,m,beta,x0)
l1 = lorentz(10,28,15,[8,4,0])
#step
#print("Backward: t={0} x={1} v={2} \n".format(t,sb.x1[-1,0],sb.x1[-1,1]))
#print("Forward: t={0} x={1} v={2} \n".format(t,sf.x1[-1,0],sf.x1[-1,1]))
#print("Trapezoid: t={0} x={1} v={2} \n".format(t,st.x1[-1,0],st.x1[-1,1]))
while t < 50:
    #xif = forwardEuler(sf,sf.x1[-1],step)
    #xib = backwardEuler(sb,sb.x1[-1],step)
    xit = trapezoid(st,st.x1[-1],step)
    xil = trapezoid(l1,l1.x1[-1],step)
    #sb.add_step(xib)
    #sf.add_step(xif)
    st.add_step(xit)
    l1.add_step(xil)
    t = t+step
    tlist.append(t)
    #print("Backward: t={0} x={1} v={2} \n".format(t,sb.x1[-1,0],sb.x1[-1,1]))
    #print("Forward: t={0} x={1} v={2} \n".format(t,sf.x1[-1,0],sf.x1[-1,1]))
    #print("Trapezoid: t={0} x={1} v={2} \n".format(t,st.x1[-1,0],st.x1[-1,1]))
fig1 = plt.figure(1)
#plt.plot(sf.x1[:,0],sf.x1[:,1],label="Forward")
#plt.plot(sb.x1[:,0],sb.x1[:,1],label="Backward")
plt.plot(st.x1[:,0],st.x1[:,1],label="Trapezoid")
plt.legend()
fig1.show()
fig2 = plt.figure(2)
ax1 = fig2.gca(projection='3d')
ax1.plot(l1.x1[:,0],l1.x1[:,1],l1.x1[:,2],label="Lorenz")
ax1.legend()
fig2.show()
raw_input()
