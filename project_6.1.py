#this function gets one argument - an integer or string that contains an integer
#and return integer - the number of "holes" in the decimal notation of this number 
#or string ERROR if the given argument does not meet the requirements
def count_holes(n):
    if isinstance(n, int):
        n = str(n)
    elif not isinstance(n, str) or not n.isdigit():
        return "ERROR"
    holes_in_number = {'0':1, '4':1, '6':1, '8':2, '9':1}
    hole_counter = 0
    string_without_beginzero = ''
    beginzero = 0
    #remove zeros at the beginning of the number
    for i in n:
        if i == '0':
            beginzero += 1
        else:
            string_without_beginzero = n[beginzero:]
            break
    if beginzero == len(n):
        string_without_beginzero = n
    for i in string_without_beginzero:
        if i in holes_in_number:
            hole_counter += holes_in_number[i]
    return hole_counter