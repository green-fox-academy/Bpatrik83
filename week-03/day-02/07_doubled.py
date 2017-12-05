# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    try:
        with open(file_name, "r") as f:
            with open(file_decrypt, "w") as dec:
                for line in f:
                    for i in range(0, len(line) - 1 , 2):
                            dec.writelines(line[i])
                    dec.writelines("\n")
        return "Decrypting done!"

    except IOError:
        return "Unable to open file!"

file_name = "duplicated-chars.txt"
file_decrypt = "decrypted.txt"
print(decrypt(file_name))
