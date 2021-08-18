import os
import glob
import csv
import pandas as pd

# giving directory name
dirname = 'INSERT DIRECTORY PATH'

# giving file extension
ext = '.txt'

# iterating over all files
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension

    else:
        continue
