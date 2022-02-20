#program gets arbitrary, non-zero, number of values - command line arguments
#and print a string consisting of the values obtained in reverse order, written through a space.
import sys

argum_list = sys.argv[1:]
argum_list.reverse()
output_string = ''
for i in argum_list:
    for j in i:
        output_string = output_string + j
    output_string = output_string + ' '
print(output_string[:-1])