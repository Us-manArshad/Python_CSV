# Find the hottest temp of every month
import os


class Weather():
    
    # Method to find maximum values from list
    def search_max(self, li):
        max_val = 0
        for i in range(len(li)):
            if max_val < li[i]:
                max_val = li[i]
        return max_val

    # Method to find hottest temperature from all files
    def search_all_files(self, DATA_DIR, hottest_temp):
        li = []
        for filename in os.listdir(DATA_DIR):
            file = os.path.join(DATA_DIR, filename)
            if hottest_temp == self.read_files(file, filename):
                li.append(filename)
        print(f"\n""Hottest Temperature of all Weather Data is : ",hottest_temp, "at month:")
        return li

    # Read files and print maximum value of inputed weather month
    def read_csv_files(self, file, filename):
        data_list =[]  
        with open(file, 'r') as data_file:  
            lines = data_file.readlines()
            for line in lines[2:]:
                if line != '\n' and line.find('<') < 0:
                    data = line.strip().split(',')
                    if data[1] != '':
                        data_list.append(int(data[1]))
            # Find the maximum temp from Max TempC 
            found = self.search_max(data_list)
            print(f"List of Temperature of Month {filename} is :""\n" f"{data_list}")
            print(f"Hottest Temperature in {filename} is : {found}","\n")
        return found

    # Same as upper fuction but this will only return maximum temp..
    def read_files(self, file, filename):
        data_list =[]
        with open(file, 'r') as data_file:  
            lines = data_file.readlines()
            for line in lines[2:]:
                if line != '\n' and line.find('<') < 0:
                    data = line.strip().split(',')
                    if data[1] != '':
                        data_list.append(int(data[1]))
            # Find the maximum temp from Max TempC 
            found = self.search_max(data_list)
        return found
       
if __name__ == "__main__":
    # Weather class object 
    weather = Weather() 
    high_temp = []
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, 'csv')
    for filename in os.listdir(DATA_DIR):
        file = os.path.join(DATA_DIR, filename)

        high_temp.append(weather.read_csv_files(file, filename))
        hottest_temp = weather.search_max(high_temp)

       # To find month of hottest temperature.
    print(weather.search_all_files(DATA_DIR, hottest_temp))
