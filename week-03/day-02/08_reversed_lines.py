# Create a method that decrypts reversed-lines.txt

def decrypt(file_rev):
    try:
        with open(file_rev, "r") as f:
            with open(file_reversed, "w") as rev:
                text = f.readlines()
                text.remove("\n")
                for i in text:
                    i[:2].replace("\n", "")
                    rev.write(i[::-1])
        return "Reversing done!"

    except IOError:
        return "Unable to open file!"


file_rev = "reversed-lines.txt"
file_reversed = "reverse-done.txt"
print(decrypt(file_rev))