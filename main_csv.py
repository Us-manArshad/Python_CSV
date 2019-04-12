import os
import csv
from datetime import datetime


class Weather:


    def read(self, path, filename):
        size  = []
        with open(path) as input_file:
            reader = csv.reader(input_file)
            lines = input_file.readlines()
            for line in lines[2:]:
                if line != '\n' and line.find('<') < 0:
                    row = line.strip().split(',')
                    if row[1] != '':
                        size.append(int(row[1]))
                #find max from li size
                maximum = max(size)
                index_list = []
                # it will print number indexes where maximum values are founds
                index_list = self.find_index(size, maximum)
                # It will print date of indexes
                index_date = []
                for i in range(len(index_list)):
                    index_date.append(str(self.find_date(index_list[i], path)))
        return index_date, filename, maximum


    def find_date(self, index, path):
        li,li1  = [],[]
        with open(path) as input_file:
            reader = csv.reader(input_file)
            lines = input_file.readlines()
            for line in lines[2:]:
                if line != '\n' and line.find('<') < 0:
                    row = line.strip().split(',')
                    row_date = datetime.strptime(row[0], "%Y-%m-%d")
                    li.append(row_date.strftime("%Y-%m-%d"))
        val = li[index]    
        return val

    
    def find_index(self, li, maximum):
        index_list = []
        for i,j in enumerate(li):
            if j == maximum:
                index_list.append(i)
        return index_list
    

if __name__ == "__main__":
    weather = Weather()
    max_list = []
    max_temp_date = []
    max_file_name = []
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, 'csv')
    for filename in os.listdir(DATA_DIR):
        file = os.path.join(DATA_DIR, filename)
        (index_date, filename, maximum) = weather.read(file, filename)
        
        max_list.append(maximum)
        max_temp = max(max_list)

    # After uper loop is terminate the second loop will run again to find the max date , filename
    for filename in os.listdir(DATA_DIR):
        file = os.path.join(DATA_DIR, filename)
        (index_date, filename, maximum) = weather.read(file, filename)
        if max_temp == maximum:
            max_temp_date.append(index_date)
            max_file_name.append(filename)
        
    print(f"The Hottset Temperature is: {max_temp} at day: {max_temp_date},\nfilenames: {max_file_name} Respectively.")
