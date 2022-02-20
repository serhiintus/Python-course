#program counts the "happy" tickets, whose numbers are in the range from first argument to second argument inclusive
#it's a tickets in which the sum of the first three digits is equal to the sum of the last three
import sys

argum_1 = int(sys.argv[1])
argum_2 = int(sys.argv[2])
counter = 0

while argum_1 <= argum_2:
    arr = list(map(int, str(argum_1)))
    if len(arr) < 6:
        for i in range(6 - len(arr)):
            arr.insert(0, 0)
    if sum(arr[0:3]) == sum(arr[3:]):
        counter += 1
    argum_1 += 1
print(counter)