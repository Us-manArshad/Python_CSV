# Function to find maximum value from the list
class Max:
    def find(li):
        maximum = 0
        for i in range(len(li)):
            if maximum < li[i]:
                maximum = li[i]
        return maximum
