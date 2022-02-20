#This function gets two arguments - positive integers n and m (0 < n, m <= 35)
#and return the n-th element of the super-Fibonacci sequence of the m order.
#A super-Fibonacci sequence of order m will be considered a sequence of numbers 
#in which each element is equal to the sum of m previous ones.
#Examples: super_fibonacci(17, 2) return 1597, super_fibonacci(9, 3) return 57
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