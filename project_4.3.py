import sys

arr = sys.argv[1]
x = 0
y = 0
chek = True
for i in arr:
    if i == '(':
        x += 1
    else:
        y += 1
    if x < y:
        chek = False
        break
if chek == True and x == y:
    print("YES")
else:
    print("NO")