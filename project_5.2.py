#this function counts the number of different digits of the number b contained in the number a
def counter(a, b):
    a = str(a)
    b = str(b)
    count = 0
    unduplicated_b = ''
    unduplicated_a = ''
    #remove duplicates in b
    for i in b:
        if i not in unduplicated_b:
            unduplicated_b += i
    #remove duplicates in a
    for i in a:
        if i not in unduplicated_a:
            unduplicated_a += i
    for i in unduplicated_b:
        for j in unduplicated_a:
            if i == j:
                count += 1
    return count
#examples:
print(counter(1234567890, 987654321)) #9
print(counter(123123123, 321456789)) #3