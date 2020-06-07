import os, datetime, serial, csv, time, random, signal
import serial.tools.list_ports
from serial import Serial

"""
    Handles Retrieving serial data from arduino
    Log all data into an appropriately names CSV files
    This can be run independently of the main graphing program
"""

# Handle automatic filename generation
date_in_title = True
tests = []
max_test_length = 25200     # Maximum length the test will run in seconds. Currently 7 Hours (25200s)

save_dir = "data"
file_list = os.listdir(save_dir)


for i in range(len(file_list)):
    file_list[i] = file_list[i][:-4]        # Remove .csv file extension
    file_list[i] = file_list[i].split('_')[-1]

for file in file_list:
    try:
        num = int(file)
        tests.append(num)
    except:
        print("ERROR: Cannot convert file: \'" , file, "\' to integer")

if len(tests) != 0:
    current_test = max(tests) + 1
else:
    current_test = 1

# Create new filename
if date_in_title:
    file_name = str(datetime.date.today()) + "-test_" + str(current_test)+".csv"
else:
    file_name = "test_" + str(current_test)+".csv"

print("Creating File:",file_name)
file_name = save_dir + "/" + file_name
print(file_name)
header = [("Cell " + str(i + 4*(current_test-1))) for i in range(1,5)]  # Create Header of CSV
header.insert(0, 'Time')

"""     Serial Setup    """
"""         This will dynamically find the arduino's serial port     """
#  Everytime the serial port is open the arduino resets
#TODO: Remove debugging prints

ports = serial.tools.list_ports.comports()
all_ports = []

for port, desc, hwid in sorted(ports):
        print("{}: {}".format(port, desc))
        all_ports.append("{}: {}".format(port, desc))

print(all_ports)
serial_port = ""
port_found = False
for p in all_ports:
    curr = p.lower()
    if 'serial' in curr:
        serial_port = p.split(':')[0]
        port_found = True

if not port_found:
    print("Arduino not found! Ending Program")
    os.kill(os.getpid(), signal.SIGTERM)
    exit()


print(serial_port)

# Open Serial Port
ser = Serial(serial_port, 9600, timeout=5)


with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)


    for i in range(max_test_length):
        writer.writerow(str(ser.readline())[2:-5].split(' '))
        f.flush()   # makes it continually write to disk. Force quitting the program wont lose data

    # When done reading, close file
    print("Data Acquisition has finished. Closing file and exiting")
    f.close()
    # Kill main when this finishes
    os.kill(os.getpid(), signal.SIGTERM)
