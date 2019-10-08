# Find the hottest/Coldest temp of every month and overall data
import os


class Weather():

    # Method to find hottest and coldest temperature from all files
    def search_all_files(self, DATA_DIR, max_temp, min_temp):
        max_months_list = []
        min_months_list = []
        for filename in os.listdir(DATA_DIR):
            file = os.path.join(DATA_DIR, filename)
            (max_temp_val, data_list, min_temp_val, data_list_min, filename) = weather.read_files(file, filename)
            if max_temp == max_temp_val:
                max_months_list.append(filename)
            if min_temp == min_temp_val:
                min_months_list.append(filename)
        return max_months_list, min_months_list

    # Read files and print maximum and minimum value of inputed weather month
    def read_files(self, file, filename):
        data_list_max = []
        data_list_min = []
        with open(file, 'r') as data_file:  
            lines = data_file.readlines()
            for line in lines[2:]:
                if line != '\n' and line.find('<') < 0:
                    data = line.strip().split(',')
                    if data[1] != '':
                        data_list_max.append(int(data[1]))
                        data_list_min.append(int(data[3]))
            # Find the maximum temp from Max TempC 
            max_temp_val = 0
            min_temp_val = 0
            for i in range(len(data_list_min[:])):
                if data_list_min[i] == '':
                    pass
                else:
                    max_temp_val = max(data_list_max)

            # Finding minimum data from Min Temprature Column
            for i in range(len(data_list_min[:])):
                if data_list_min[i] == '':
                    pass
                else:
                    min_temp_val = min(data_list_min)
                    
        return max_temp_val, data_list_max, min_temp_val, data_list_min, filename


if __name__ == "__main__":
    # Weather class object 
    weather = Weather() 
    max_temp_list = []
    min_temp_list = []
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, 'csv')
    for filename in os.listdir(DATA_DIR):
        file = os.path.join(DATA_DIR, filename)

        (max_temp_val, data_list_max,min_temp_val, data_list_min, filename) = weather.read_files(file, filename)
        max_temp_list.append(max_temp_val)
        max_temp = max(max_temp_list)
        min_temp_list.append(min_temp_val)
        min_temp = min(min_temp_list)
        print(f"List of Temperature of Month {filename} is :""\n" f"{data_list_max}")
        print(f"Highest/Hottest Temperature in {filename} is : {max_temp_val} ")
        print(f"Lowest/Coldest Temperature in {filename} is : {min_temp_val} \n")

    # To find month of hottest temperature.
    (max_months_list, min_months_list) = weather.search_all_files(DATA_DIR, max_temp, min_temp)
    print("\n\n!----------------------------Maximum or Hottest Temperature------------------------------!")
    print(f"The maximum temperature of all the files data is: {max_temp} at months: \n{max_months_list}")

    print("\n\n!----------------------------Minimum or Coldest Temperature------------------------------!")
    print(f"The minimum temperature of all the files data is: {min_temp} at months: \n{min_months_list}\n\n")

    
    print("Attention: Those fields which are empty are not included for transparency of data. !! Thank you")
