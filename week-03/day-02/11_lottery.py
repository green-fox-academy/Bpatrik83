# Create a method that find the 5 most common lottery numbers otos.csv

def five_most_frequent(file_name):
    dict = {}
    with open(file_name) as fo:
        for line in fo.readlines():
            for i in range(5):
                if not line.rstrip("\n").split(";")[11+i] in dict:
                    dict[line.rstrip("\n").split(";")[11+i]] = 1
                else:
                    dict[line.rstrip("\n").split(";")[11+i]] +=1
        s_dict = [(k, dict[k]) for k in sorted(dict, key=dict.get, reverse=True)]
        return s_dict[:5]

file_name = "otos.csv"
print(five_most_frequent(file_name))