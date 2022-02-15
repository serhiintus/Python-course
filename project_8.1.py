class CombStr(object):
    def __init__(self, basic_string):
        self.basic_string = basic_string
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


s0 = CombStr('?')
print(s0.count_substrings(1))
s3  = CombStr('qweqweqwe')
print(s3.count_substrings(4))
