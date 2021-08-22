import pandas as pd

#  This script takes in one text file and converts to a CSV.

read_file = pd.read_csv(r'/Users/dblue/PycharmProjects/hmg3/txtToCSVFileConverter/batchTextFiles/7-23-Unplanned-Solar-Outage/solar pv.txt')
read_file.to_csv(r'/Users/dblue/PycharmProjects/hmg3/txtToCSVFileConverter/batchTextFiles/7-23-Unplanned-Solar-Outage/solar pv.csv', index=None)

# battery SOC.txt
# battery.txt
# busbar frequency.txt
# busbar voltage.txt
# inverter.txt
# load.txt
# solar pv.txt
# time series to 1 min avg