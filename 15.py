import numpy as np
import matplotlib.pyplot as plt

def proba(x_value, sigma):
    return (1/(sigma * np.sqrt(2.0 * np.pi))) * np.exp(-0.5*(x_value/sigma)**2)

def likelihood(x_values, sigma):
    like = (1.0/9.0)*sigma/sigma
    for i in x_values:
        like = like * proba(i, sigma)
    return like

data = np.loadtxt('valores.txt')

n_points = 10**5
sigma = np.linspace(1,10,n_points)
l = likelihood(data, sigma)
plt.figure()
plt.plot(sigma,l)
plt.xlabel(r"$\sigma$")
plt.ylabel(r"$L\times {\rm{prob} (\sigma)}$")
plt.savefig("sigma.png")

plt.hist(likelihood(data,sigma), bins=30, density=True)