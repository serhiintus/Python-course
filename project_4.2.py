import sys

x = sys.argv[1:]
xy = x [::-1]
y = ''
for i in range(len(xy)):
    for j in xy[i]:
        y = y + j
    y = y + ' '
d = y[:-1]
print(d)
