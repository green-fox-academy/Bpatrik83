# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

def printer_texts(*args):
    sumtext = ""
    for i in args:
        sumtext += i + " "
    print(sumtext)

def printer_nums(*args):
    sumnums = 0
    for i in args:
        sumnums += i
    print(sumnums)

printer_texts("Hello")
printer_texts("Hello", "GreenFox")
printer_texts("Hello", "GreenFox", "Good", "Day")
printer_nums(1 ,2 ,3 ,4, 5, 6, 7, 8 , 9, 10)