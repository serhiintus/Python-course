#program gets a string, ignore cases and spaces, and print "YES" if string is a palindrom or "NOT" if it's not.
import sys

x = sys.argv[1].lower()
y = ''
for l in x:
    if l != ' ':
        y = y + l
a = int(len(y)/2)
j = len(y)-1
b = True
for i in range(a):
    if y[i] != y[j]:
        b = False
        break
    j -= 1
if b == True:
    print("YES")
else:
    print("NO")