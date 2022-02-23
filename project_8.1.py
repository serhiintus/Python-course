#class CombStr represents a string of characters
class CombStr(object):
    #constructor gets 1 argument - string
    def __init__(self, basic_string):
        self.basic_string = basic_string
    #this method gets 1 argument a non-negative integer, and returns 
    #the number of all different substrings with length equal to argument contained in the string
    def count_substrings(self, length):
        if length == 0 or length > len(self.basic_string):
            return 0
        begin, end, list_parts = 0, length, []
        while end <= len(self.basic_string):
            if self.basic_string[begin:end] not in list_parts:
                list_parts.append(self.basic_string[begin:end])
            begin += 1
            end += 1
        return len(list_parts)

#EXAMPLES:
s0 = CombStr('qqqqqqweqqq%')
print (s0.count_substrings(0)) # 0
print (s0.count_substrings(1)) # 4
print (s0.count_substrings(2)) # 5
print (s0.count_substrings(5)) # 7
print (s0.count_substrings(15)) # 0