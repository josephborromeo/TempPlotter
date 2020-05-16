import os, datetime, serial, csv, time, random

"""
    Handles Retrieving serial data from arduino
    Log all data into an appropriately names CSV files
"""

# Handle automatic filename generation
date_in_title = True
tests = []

save_dir = "data"
file_list = os.listdir(save_dir)


for i in range(len(file_list)):
    file_list[i] = file_list[i][:-4]        # Remove file extension
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

with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    t = 30
    for i in range(t):
        writer.writerow([i] + list(int(60*random.random()) for j in range(4)))
        time.sleep(0.01)