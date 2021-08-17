import os
import glob
import csv
import pandas as pd

# giving directory name
dirname = '/Users/dblue/PycharmProjects/hmg3/txtToCSVFileConverter/batchTextFiles/7-21-Planned-Solar-Outage'

# giving file extension
ext = ('.txt')

# iterating over all files
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
    else:
        continue
