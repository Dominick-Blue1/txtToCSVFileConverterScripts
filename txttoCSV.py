import pandas as pd

#  This script takes in one text file and converts to a CSV.

read_file = pd.read_csv(r'insert the pathway to the text file here/sample1.txt')
read_file.to_csv(r'insert desired pathway to new CSV file location here/newCSV.csv', index=None)
