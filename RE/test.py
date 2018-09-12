import numpy as np
import matplotlib.pyplot as plt

Melt = np.loadtxt('./test.txt', skiprows=1)
labels = ['Temp', 'E_pair', 'E_mol', 'TotEng', 'Press']
for i, label in enumerate(labels, start=1):
    plt.plot(Melt[1:, 0], Melt[1:, i], label=label)
    plt.legend()
plt.show()
