import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from serial import Serial
import winsound
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import csv



freq = 2500
duration = 500

"""         To dynamically find arduino serial port     
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
"""






"""
*****     Buzzer Code     *****

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

f = open('data/2020-05-20-test_1.csv', 'r')
reader = csv.reader(f)
print(reader.line_num)
print(reader)
for row in reader:
    pass

last = row
print(last)
f.close()
