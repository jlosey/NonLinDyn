#Time Series Embedding 
#import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

def readData(fname):
    """Read in data to be embedded"""
    X = []
    f = open(fname,'r')
    for line in f:
        X.append(float(line.strip()))
    return X

def embed(data,tau,m):
    """Time series embedding algorithm"""   
    E=[]
    for i in range(0,len(data)-m*tau):
        v = []
        for j in range(0,m):
            try:
                v.append(data[i+j*tau])
            except IndexError:
                pass
            continue
        E.append(v)
    return E


def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    #line.axes.axis([0, 10, 0, 1])
    return line,

plt.figure()
plt.ion()
ts = readData("amplitude.dat")
for t in range(1,350):
    tsE = embed(ts,t,7)
    x = [row[0] for row in tsE]
    y = [row[2] for row in tsE]
    plt.cla()
    plt.plot(x,y)
    plt.pause(0.025)
    plt.show()
    #raw_input()
