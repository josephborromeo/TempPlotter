import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

"""
                        PLAYGROUND FOR TESTING RANDOM CODE
"""


matplotlib.use('TkAgg')
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(12.8, 7.2))
plt.tight_layout(5)


fig.canvas.manager.window.wm_geometry("+320+148")       # Center Plot in Frame

fig.set_figwidth(12.8)
fig.set_figheight(7.2)

x_len = 1000
y_range = [0, 70]
ax.autoscale()
#ax.set_ylim(0,70)


# xs = np.arange(0,x_len, 1)
# ys = [25]*x_len

xs = []
ys = []

line, = ax.plot(xs, ys, 'r')
ax.autoscale()

plt.title('Cell Temp over Time')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (deg C)')


def animate(i, ys,xs, start_time):
    #data = (20*math.sin((i/5)%100) + 40)  # Arbitrary data which will be replaced by sensor data
    #data = 10*math.sin(i/5.0) + 25 # Arbitrary data which will be replaced by sensor data
    data = math.sqrt(i)
    xs.append(i)
    ys.append(data)

    line.set_xdata(xs)  # update the data.
    line.set_ydata(ys)  # update the data.
    ax.autoscale(True)
    # line2.set_ydata(-y)  # update the data
    return line,

start = time.clock()
ani = animation.FuncAnimation(
    fig, animate, interval=5,fargs=(ys,xs, start, ), blit=True)

plt.show()