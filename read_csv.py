from find_max import Max
class ReadFiles:
    # Function that read files and return maximum    
    def read_csv_files(file, filename):
        data_list =[]  
        with open(file, 'r') as data_file:  
            lines = data_file.readlines()
            for line in lines[2:]:
                if line != '\n' and line.find('<') < 0:
                    data = line.strip().split(',')
                    if data[1] != '':
                        data_list.append(int(data[1]))
                        
            # Find the maximum temp from Max TempC 
            found = Max.find(data_list)
            print(data_list)
            print(f"Hottest Temperature in {filename} is :", found,"\n")
            
        return data_list

  
