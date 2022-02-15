class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        if len(self) < 1 or len(s) < 1:
            return False
        number_of_repeat = self.count(s)
        length_of_object = len(self)
        length_of_received_str = len(s)
        if number_of_repeat == length_of_object/length_of_received_str and length_of_object%length_of_received_str == 0:
            return True
        else:
            return False
    def is_palindrom(self):
        if len(self) < 1:
            return True
        str_low_case = self.lower()
        j = len(str_low_case) - 1
        for i in range(len(str_low_case)//2):
            if str_low_case[i] != str_low_case[j]:
                return False
            j -= 1
        return True


string_basic = SuperStr('q')
print(string_basic.is_repeatance('q'))

