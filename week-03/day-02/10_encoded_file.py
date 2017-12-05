# Create a method that decrypts encoded-lines.txt
def decrypt(file_name):
    try:
        with open(file_name, "r") as f:
            with open(file_encrypt, "w") as rev:
                for lines in f:
                    s = ""
                    for i in lines:
                        i = ord(i)
                        if i != 32:
                                i = chr(i - 1)
                                s += i
                        else:
                            s += " "
                    rev.writelines(s + "\n")

        return "Reversing done!"

    except IOError:
        return "Unable to open file!"


file_name = "encoded-lines.txt"
file_encrypt = "encoded_done.txt"
print(decrypt(file_name))