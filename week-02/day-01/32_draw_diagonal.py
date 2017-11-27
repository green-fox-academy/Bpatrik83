
# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

num = input("Enter a number: ")
num = int(num)
str = "%" * num
within_space = num - 2
space = " " * num

print(str)

for i in range(within_space):
    print(str[0] + space[:i] + str[0] + space[:num - i - 3] + str[0])
print(str)