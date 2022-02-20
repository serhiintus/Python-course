#This function gets three arguments - first is integer or string, which represents number, 
#second is the radix of the number system to which the first argument belongs, 
#third is the radix of the number system (1 <= n, m <= 36)
#and returns string - the representation of first argument in number system with radix third argument.
#If the first argument is not a number or a string, or cannot be a non-negative integer 
#represents in a number system based on second argument, function returns the logical constant False.
def convert_n_to_m(x, n, m):
    convert_num = ''
    if isinstance(x, int) and x >= 0:
        convert_num = str(x).upper()
    elif isinstance(x, str):
        convert_num = x.upper()
    else:
        return False
    to_decimal = {'0':0, '1':1, '2':2, '3':3, '4':4, 
			'5':5, '6':6, '7':7, '8':8, '9':9, 
			'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 
			'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 
			'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 
			'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 
			'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
    from_decimal = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 
			5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 
			10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 
			15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 
			20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 
			25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 
			30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
    alfa_to_num = []
    [alfa_to_num.append(to_decimal[i]) for i in convert_num]
    for i in alfa_to_num:
        if i >= n:
            return False
    pow_to_convert = len(alfa_to_num) - 1
    decimal_list = []
    for i in alfa_to_num:
        decimal_list.append(i * n ** pow_to_convert)
        pow_to_convert -= 1
    decimal_num = sum(decimal_list)
    converted_num_list = []
    if decimal_num == 0:
        return '0'
    if m < 2:
        converted_num_list = [0] * decimal_num
        return ''.join([str(i) for i in converted_num_list])
    else:
        while decimal_num > 0:
            converted_num_list.append(from_decimal[decimal_num % m])
            decimal_num = decimal_num // m
        converted_num_list.reverse()
        return ''.join(converted_num_list)
#Examples:    
print(convert_n_to_m(777, 10, 2)) #result 1100001001
print(convert_n_to_m('11111', 10, 16)) #result 2B67
print(convert_n_to_m('7e6', 16, 2)) #result 11111100110
print(convert_n_to_m('ZZZZ', 36, 13)) #result 46A672
print(convert_n_to_m(-25, 10, 2)) #result False