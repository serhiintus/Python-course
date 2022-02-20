#program gets a string, ignore cases and spaces, and print "YES" if string is a palindrom or "NOT" if it's not.
import sys

argum = sys.argv[1].lower()
text_to_check = ''
for i in argum:
    if i != ' ':
        text_to_check += i
j = len(text_to_check)-1
check = True
for i in range(len(text_to_check)//2):
    if text_to_check[i] != text_to_check[j]:
        check = False
        break
    j -= 1
if check == True:
    print("YES")
else:
    print("NO")