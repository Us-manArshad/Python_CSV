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
                
                maximum = self.find_max(size)
                index_list = []
                # it will print number indexes where maximum values are founds
                index_list = self.find_index(size)
                # It will print date of indexes
                index_date = []
                for i in range(len(index_list)):
                    index_date.append(str(self.find(index_list[i], path)))
                
            print("Maximum Temp of month:",filename," is: ",maximum, "at Dates: ", index_date)
        return maximum

    
    def find(self, index, path):
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


    def find_max(self,li):
        maximum = 0
        for i in range(len(li)):
            if maximum <= li[i]:
                maximum = li[i]
        return maximum
    

    def find_index(self, li):
        Maximum = self.find_max(li)
        index_list = []
        for i,j in enumerate(li):
            if j == Maximum:
                index_list.append(i)
        return index_list
    

if __name__ == "__main__":
    weather = Weather()
    max_list = []
    max_temp_list = []
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, 'csv')
    for filename in os.listdir(DATA_DIR):
        file = os.path.join(DATA_DIR, filename)
        
        max_list.append(weather.read(file, filename))
        max_temp = max(max_list)
        
    print("The Hottset is: ", max_temp)
