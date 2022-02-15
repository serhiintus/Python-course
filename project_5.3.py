def super_fibo(n, m):
    if n > m:
        list_fibo = [1 for i in range(m)]
        x = 0
        for i in range(m, n):
            list_fibo.append(sum(list_fibo[x:i]))
            x += 1
        return list_fibo[n -1]
    else:
        return 1
a, b = 8, 2
print(super_fibo(a, b))