import math
import matplotlib.pyplot as plt

t = [i+1 for i in range(200)]
s = [math.sin(i) for i in t]
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('simple plotting test')
plt.grid(True)
plt.show()
