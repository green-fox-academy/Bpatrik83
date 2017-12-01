"""Exercise

Write a function to solve Josephus Problem. The program should ask for a number,
this number represents how many people are in the "game". T
he return value should be the number of the "winning" seat.
Examples
        number of people 	number of the winning seat
              1 	                1
              2 	                1
              3 	                3
              7                  	7
             12 	                9
             41 	                19                                                                              """



def josephus_problem(number):
    binary_number = bin(number)[2:]                         # 41 to binary equal 101001
    binary_number = "1" + "0" * (len(binary_number) - 1)    # change ones to zeros except the first
    binary_number = int(binary_number, 2)                   # 100000 to decimal equal 32
    result = (2 * (number - binary_number) + 1)             # solution formula
    return result                                           # the result

print(josephus_problem(41))                                 # input number 41

