import os, glob
import csv
import numpy as np

# Get time, Max temp for each cell. E.g:
# C1  -  37C
# C2  -  32C
# C3  -  35C
# C4  -  33C
os.chdir("data")
files = glob.glob("*.csv")

cells = []
temps = []
for file in files:
    temp = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            temp.append(row)

        cells.extend(temp[0][1:])
        temp = np.array(temp[1:], dtype=np.float16)
        temps.extend(temp.max(axis=0)[1:])

        f.close()

for i in range(len(cells)):
    print(str(cells[i])+": " + str(temps[i]) +"C")

print("Average Max temp = " + str(np.average(temps)) + "C")
print("Max temp Recorded = " + str(np.max(temps)) + "C")
print("Min Max temp = " + str(np.min(temps)) + "C")