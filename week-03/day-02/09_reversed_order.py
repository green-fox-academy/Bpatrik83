# Create a method that decrypts reversed-order.txt

def order_lines(file_order):
    try:
        with open(file_order, "r") as f:
            with open(file_reversed, "w") as rev:
                s = f.readlines()
                s.reverse()
                s[0] += "\n"
                for i in range(len(s)):
                    rev.writelines(s[i])

        return "Ordered done!"

    except IOError:
        return "Unable to open file!"


file_order = "reversed-order.txt"
file_reversed = "order-done.txt"
print(order_lines(file_order))