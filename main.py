import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, winsound, _thread, csv, os


# FIXME: This is pretty sloppy, should fix the communication architecture and avoid this all together
def get_data(x):
    import fetch_data

_thread.start_new_thread(get_data, (1,))

def get_last():
    file = os.listdir('data')[-1]       # FIXME: Won't work past 9 tests, must base off test number
    print('OPENING', file)
    f = open('data/' + str(file), 'r')
    reader = csv.reader(f)
    row = []
    for row in reader:
        row
    print('DATA: ',row)
    last = row[1:]
    f.close()
    return float(last[0]), float(last[1]), float(last[2]), float(last[3])

matplotlib.use('TkAgg')
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(12.8, 7.2))
plt.tight_layout(2) 

fig.canvas.manager.window.wm_geometry("+320+148")       # Center Plot in Frame

fig.set_figwidth(12.8)
fig.set_figheight(7.2)

"""     Setup Safety Beeps"""
freq = 2500
duration = 20
global max_vol
max_vol = False


""" PARAMS """

x_len = 600         # Time in seconds to plot
temp_range = [0, 70]
line_width = 2

show_temp_lim = True
temp_lim = 65

if show_temp_lim:
    plt.plot([0,x_len], [temp_lim, temp_lim], 'orange', linewidth = 2.5, linestyle='dashed')


ax.set_ylim(temp_range[0], temp_range[1])
ax.set_xlim(0, x_len)
ax.yaxis.grid()

xs = np.arange(0, x_len, 1)

x_com = []
temp_data_1 = []
temp_data_2 = []
temp_data_3 = []
temp_data_4 = []

# TODO: Create these dynamically
temp1, = ax.plot(x_com, temp_data_1, 'r', linewidth=line_width)
temp2, = ax.plot(x_com, temp_data_2, 'lightgreen', linewidth=line_width)
temp3, = ax.plot(x_com, temp_data_3, 'c', linewidth=line_width)
temp4, = ax.plot(x_com, temp_data_4, 'fuchsia', linewidth=line_width)

temp1_label = ax.text(35,67, "CELL 1:", fontsize=15, color='r')
temp2_label = ax.text(185,67, "CELL 2:", fontsize=15, color='lightgreen')
temp3_label = ax.text(335,67, "CELL 3:", fontsize=15, color='c')
temp4_label = ax.text(485,67, "CELL 4:", fontsize=15, color='fuchsia')


# transform=plt.gcf().transFigure
plt.title('Cell Temp over Time')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (deg C)')

time.sleep(4)

def animate(i, t1, t2, t3, t4,x_com):

    data1, data2, data3, data4 = get_last()
    # data1 = math.sqrt(i ** 1.2) % 20  # Arbitrary data which will be replaced by sensor data
    # data2 = math.sqrt(i) % 20  # Arbitrary data which will be replaced by sensor data
    # data3 = 5 * math.sin(i / 5.0) + 60  # Arbitrary data which will be replaced by sensor data
    # data4 = 10 * math.cos(i / 12.0) + 30  # Arbitrary data which will be replaced by sensor data

    # TODO: Store and update everything in a loop to prevent messy copy and pasting


    if i > x_len:
        del t1[0]
        del t2[0]
        del t3[0]
        del t4[0]

    else:
        x_com.append(i)
        temp1.set_xdata(x_com)  # update the data.
        temp2.set_xdata(x_com)  # update the data.
        temp3.set_xdata(x_com)  # update the data.
        temp4.set_xdata(x_com)  # update the data.

    t1.append(data1)
    t2.append(data2)
    t3.append(data3)
    t4.append(data4)

    temp1.set_ydata(t1)  # update the data.
    temp2.set_ydata(t2)  # update the data.
    temp3.set_ydata(t3)  # update the data.
    temp4.set_ydata(t4)  # update the data.

    # --- Current Cell Temps --- #
    temp1_label.set_text("CELL 1: %.2f"%(t1[-1]))
    temp2_label.set_text("CELL 2: %.2f"%(t2[-1]))
    temp3_label.set_text("CELL 3: %.2f"%(t3[-1]))
    temp4_label.set_text("CELL 4: %.2f"%(t4[-1]))

    return temp1, temp2, temp3, temp4, temp1_label, temp2_label, temp3_label, temp4_label,

start = time.clock()
# TODO: Evaluate whether arduino actually updaes @ 1000ms or if timing needs to be adjusted due to duplicate measurements
ani = animation.FuncAnimation(fig, animate, interval=1000, fargs=(temp_data_1, temp_data_2, temp_data_3, temp_data_4,x_com,), blit=True)


plt.show()


