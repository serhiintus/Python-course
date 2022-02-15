def count_holes(n):
    if isinstance(n, int):
        n = str(n)
    elif not isinstance(n, str) or not n.isdigit():
        return "ERROR"
    dict_zero = {'0':1, '4':1, '6':1, '8':2, '9':1}
    counter_zero = 0
    string_without_beginzero = ''
    t = 0
    for i in n:
        if i == '0':
            t += 1
        elif i != '0':
            string_without_beginzero = n[t:]
            break
    if t == len(n):
        string_without_beginzero = n
    for i in string_without_beginzero:
        if i in dict_zero:
            counter_zero += dict_zero[i]
    
    return counter_zero