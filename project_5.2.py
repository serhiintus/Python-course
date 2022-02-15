def counter(a, b):
    a = str(a)
    b = str(b)
    n = 0
    count = 0
    ax = ''
    for i in b:
        if i not in ax:
            ax += i
    for i in ax:
        for j in a:
            if i == j:
                n += 1
        if n > 0:
            count += 1
            n = 0
    return count

x = 98123560
y = 79266
print(counter(x, y))
