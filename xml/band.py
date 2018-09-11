# -*- coding: utf-8 -*-
# @Author: kyqia
# @Date:   2017-12-04 23:41:41
# @Last Modified by:   kyqia
# @Last Modified time: 2017-12-05 20:25:32
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data', usecols=range(1, 12))
np.save('G2X', data[58:119, :])
k = data[0:119, 0]
BE = data[0:119, 3:]
k[0:59] *= -np.sqrt(3)
k[59:] *= 2

plt.plot(k, BE)
plt.plot(k, np.zeros(len(k)), '--')
plt.grid(True, axis='x', ls='--')
plt.title("Band Energy v.s Sampling Point", fontsize='xx-large')
plt.xlabel("Point in k-space", fontsize='x-large')
plt.xticks([k[0], 0, k[-1]], ['L', '$\Gamma$', 'X'])
plt.ylabel("Band energy(eV)", fontsize='x-large')
plt.savefig('Band.png', dpi=200)
plt.show()
