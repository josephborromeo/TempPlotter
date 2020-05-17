import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from serial import Serial
import winsound
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


freq = 2500
duration = 500

"""         To dynamically find arduino serial port     """
#  Everytime the serial port is open the arduino resets
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

all_ports = []

for port, desc, hwid in sorted(ports):
        print("{}: {}".format(port, desc))
        all_ports.append("{}: {}".format(port, desc))

print(all_ports)
serial_port = ""
for p in all_ports:
    curr = p.lower()
    if 'serial' in curr:
        serial_port = p.split(':')[0]

print(serial_port)

ser = Serial(serial_port, 9600, timeout=5)




def set_max_volume():
    from ctypes import POINTER, cast
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import (AudioUtilities, IAudioEndpointVolume)

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    print(volume.GetMasterVolumeLevel())

set_max_volume()

while ser.is_open:
    print(str(ser.readline())[2:-5])
    winsound.Beep(freq, duration)


"""
                        PLAYGROUND FOR TESTING RANDOM CODE
"""
"""
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import (AudioUtilities, IAudioEndpointVolume)

def set_max_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(0, None)


"""



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
"""