import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("TF.dat")
s = np.shape(data)
C = s[1]
F = s[0]
lista = []

for i in range(F):
    promedio = 0
    for j in range(C):
        promedio += data[i][j]
    lista.append(promedio)

##plt.plot(data[:,0], promedio)

plt.plot(data[:,0], data[:,1])
plt.xlabel('time(y)')
plt.ylabel('Manchas Solares')
plt.savefig("solar.png")

