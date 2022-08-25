# Path
#from .utils import Utils
import os
#import pandas as pd


path = "C:/Users/Mdiallo/Documents/Master AI Datascience/MASTER1/data_collection/COURS19AOUT2022/DATA-COLLECTION-DIT/COURSE/DATABASES/data-_zJ9Zko2Dh1LYlNNgALKE.csv"
  
# Path of Start directory
start = "C:/Users/Mdiallo/Documents/Master AI Datascience/MASTER1/data_collection/COURS19AOUT2022/DATA-COLLECTION-DIT"
  
# Compute the relative file path
# to the given path from the 
# the given start directory.
relative_path = os.path.relpath(path, start)
  
# Print the relative file path
# to the given path from the 
# the given start directory.
print(relative_path)


#data =pd.read_csv(relative_path)
#print(data)
  