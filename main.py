
# Find the hottest temp of every month
import os
from find_max import Max
from read_csv import ReadFiles
from read_csv_all import Find


class Main:
    high_temp = []
    if __name__ == "__main__":
        
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        DATA_DIR = os.path.join(ROOT_DIR, 'csv')
        for filename in os.listdir(DATA_DIR):
            file = os.path.join(DATA_DIR, filename)
                        
            high_temp.append(Max.find(ReadFiles.read_csv_files(file, filename)))
            hottest_temp = Max.find(high_temp)
            
       # To find month of hottest temperature.
        Find.find_all(DATA_DIR, hottest_temp)
         


        
