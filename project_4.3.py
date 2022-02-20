#program gets a string consisting of parentheses and
#check whether a string has matching pair of parentheses or not
#the matching is true if the left parenthesis is followed by the right parenthesis
import sys

parentheses = sys.argv[1]
count_left = 0
count_right = 0
matching = True
for i in parentheses:
    if i == '(':
        count_left += 1
    else:
        count_right += 1
    if count_left < count_right:
        matching = False
        break
if matching == True and count_left == count_right:
    print("YES")
else:
    print("NO")