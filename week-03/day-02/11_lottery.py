# Create a method that find the 5 most common lottery numbers otos.csv

def five_most_frequent(file_name):
    lottery_dictionary = {}
    with open(file_name) as open_file:
        for line in open_file.readlines():
            for i in range(5):
                if not line.rstrip("\n").split(";")[11+i] in lottery_dictionary:
                    lottery_dictionary[line.rstrip("\n").split(";")[11+i]] = 1
                else:
                    lottery_dictionary[line.rstrip("\n").split(";")[11+i]] +=1
        sorted_dictionary = [(k, lottery_dictionary[k]) for k in sorted(lottery_dictionary, key=lottery_dictionary.get, reverse=True)]
        return sorted_dictionary[:5]

file_name = "otos.csv"
print(five_most_frequent(file_name))