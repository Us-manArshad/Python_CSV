import os

class EnglishWords():

    # Read files and find lenght of lengthy words of inputed words list
    def read_files(self, file, filename):
        words_list =[]
        with open(file, 'r') as data_file:  
            lines = data_file.readlines()
            for line in lines[2:]:
                if line != '\n' and line.find('<') < 0:
                    data = line.strip()
                    words_list.append(data)
            # Function call to find max length word and its length.
            (word, word_length) = self.lengthy_word(words_list)
            print(word, word_length)

            # Funtion call to find consonant and lenghty consonant.
            (consonant_word, consonant_word_len) = self.consonant_word(words_list)
            print(consonant_word, consonant_word_len)
        return words_list
                    
    # Find the lenghty word from the word_list and its lenght.
    def lengthy_word(self, words_list):
        sorted_words = sorted(words_list, key = len)
        return sorted_words[-1], len(sorted_words[-1])

    # Find all the consonants from words_list and find lenghty words and its lenght. 
    def consonant_word(self, words_list):
        consonant_list = []
        for word in words_list:
            vowels=0
            for i in word:
                if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                    vowels=vowels+1
            if vowels == 0:
                consonant_list.append(word)
        sorted_consonant_list = sorted(consonant_list, key = len)
        return sorted_consonant_list[-1], len(sorted_consonant_list[-1])
        

if __name__ == "__main__":
    # Class object 
    words = EnglishWords() 
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, 'words')
    for filename in os.listdir(DATA_DIR):
        file = os.path.join(DATA_DIR, filename)
        words.read_files(file, filename)
    
