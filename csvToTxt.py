import csv
import os


dir_name = '/Users/tianhan/Documents/ColumbiaU/Spring15/Adv_Big_Data_Analytics/Project/Reviews'
base_filename = 0
filename_suffix = 'txt'
with open('/Users/tianhan/Documents/ColumbiaU/Spring15/Adv_Big_Data_Analytics/Project/critics.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Ignore first row

    for row in reader:
        base_filename = base_filename + 1
        base_filename_temp = str(base_filename)
        txt = open(os.path.join(dir_name, base_filename_temp + "." + filename_suffix),'w+')
        txt.write(row[6])
