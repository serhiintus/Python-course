#program gets one argument that is >= 0, and print the value of the Fibonacci sequence
import sys

a = 0
b = 1
c = 0
n = int(sys.argv[1])
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    print(c) 

