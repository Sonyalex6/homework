import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7, 4))
f, ax = plt.subplots(2, 2)
f.set_size_inches(7, 4)
f.set_facecolor('#eee')
ax[0, 0].plot(np.arange(0, 5, 0.2))
ax[0, 0].grid()
ax[0, 1].plot(np.arange(5, 0, -0.2))
ax[0, 1].grid()
plt.show()