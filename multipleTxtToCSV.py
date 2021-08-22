import os
import csv
import pandas as pd

directory = os.listdir('/Users/dblue/PycharmProjects/hmg3/txtToCSVFileConverter/batchTextFiles/7-21-Planned-Solar-Outage')

for file in directory:
    if file.endswith('.txt'):
        print(file)
        file.replace('.txt', '.csv')
        print(file)
# iterating over all files
    # for filename in files:
    #     filepath = subdir + os.sep + filename
    #
    #     if filepath.endswith(".jpg") or filepath.endswith(".png"):
    #         print (filepath)

