# Create a method that decrypts encoded-lines.txt
def decrypt(file_name):
    try:
        with open(file_name, "r") as open_file:
            with open(file_encrypt, "w") as write_file:
                for lines in open_file:
                    tmp_str = ""
                    for char_i in lines:
                        char_i = ord(char_i)
                        if char_i != 32:
                                char_i = chr(char_i - 1)
                                tmp_str += char_i
                        else:
                            tmp_str += " "
                    write_file.writelines(tmp_str + "\n")
        return "Reversing done!"
    except IOError:
        return "Unable to open file!"

file_name = "encoded-lines.txt"
file_encrypt = "encoded_done.txt"
print(decrypt(file_name))