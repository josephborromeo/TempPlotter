import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

matplotlib.use('TkAgg')
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(12.8, 7.2))
plt.tight_layout(2) 

fig.canvas.manager.window.wm_geometry("+320+148")       # Center Plot in Frame

fig.set_figwidth(12.8)
fig.set_figheight(7.2)

""" PARAMS """

x_len = 600         # Time in seconds to plot
temp_range = [0, 70]
line_width = 2

ax.set_ylim(temp_range[0], temp_range[1])
ax.set_xlim(0, x_len)
ax.yaxis.grid()

xs = np.arange(0, x_len, 1)

x_com = []
temp_data_1 = []
temp_data_2 = []
temp_data_3 = []
temp_data_4 = []

temp1, = ax.plot(x_com, temp_data_1, 'r', linewidth=line_width)
temp2, = ax.plot(x_com, temp_data_2, 'lightgreen', linewidth=line_width)
temp3, = ax.plot(x_com, temp_data_3, 'c', linewidth=line_width)
temp4, = ax.plot(x_com, temp_data_4, 'fuchsia', linewidth=line_width)


plt.title('Cell Temp over Time')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (deg C)')


def animate(i, t1, t2, t3, t4,x_com):
    data1 = math.sqrt(i**1.2) % 20# Arbitrary data which will be replaced by sensor data
    data2 = math.sqrt(i) % 20# Arbitrary data which will be replaced by sensor data
    data3 = 5*math.sin(i/5.0) + 60 # Arbitrary data which will be replaced by sensor data
    data4 = 10*math.cos(i/12.0) + 30 # Arbitrary data which will be replaced by sensor data

    if i > x_len:
        del t1[0]
        del t2[0]
        del t3[0]
        del t4[0]

    else:
        x_com.append(i)

    t1.append(data1)
    t2.append(data2)
    t3.append(data3)
    t4.append(data4)

    temp1.set_ydata(t1)  # update the data.
    temp2.set_ydata(t2)  # update the data.
    temp3.set_ydata(t3)  # update the data.
    temp4.set_ydata(t4)  # update the data.

    temp1.set_xdata(x_com)  # update the data.
    temp2.set_xdata(x_com)  # update the data.
    temp3.set_xdata(x_com)  # update the data.
    temp4.set_xdata(x_com)  # update the data.


    return temp1, temp2, temp3, temp4,

start = time.clock()
ani = animation.FuncAnimation(
    fig, animate, interval=10, fargs=(temp_data_1, temp_data_2, temp_data_3, temp_data_4,x_com,), blit=True)


plt.show()