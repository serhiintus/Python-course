#class SuperStr inherits the functionality of the standard type string and contains 2 new methods
class SuperStr(str):
    #this method gets 1 argument and returns True or False depending on whether the current string can be obtained 
    #by an integer number of iterations of the argument. Returns False if argument is not a string
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
    #this method returns True or False depending on whether the string is a palindrome. Method ignores letter case.
    #An empty string is considered a palindrome
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

#EXAMPLES:
s = SuperStr('123123123123')
print (s.is_repeatance('123')) # True
print (s.is_repeatance('123123')) # True
print (s.is_repeatance('123123123123')) # True
print (s.is_repeatance('12312')) # False
print (s.is_repeatance(123)) # False
print (s.is_palindrom()) # False
print (s) # 123123123123 (string)
print (int(s)) # 123123123123 (integer)
print (s + 'qwe') # 123123123123qwe
p = SuperStr('123_321')
print (p.is_palindrom()) # True

