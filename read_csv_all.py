#finds maximum temp from all files and show month
import os
from find_max import Max
from read_csv import ReadFiles
class Find:
    

    def find_all(DATA_DIR, hottest_temp):
        li = []
        for filename in os.listdir(DATA_DIR):
            file = os.path.join(DATA_DIR, filename)
            if hottest_temp == Max.find(ReadFiles.read_files(file, filename)):
                li.append(filename)
        
        return print(f"The overall Hottest Temperature is:- {hottest_temp} at months:- {li}")
    
