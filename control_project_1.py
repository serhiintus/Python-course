import sys

coded_text = sys.argv[1]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
decoded_text = ''
temp = ''
temp_list = []

for i in coded_text:
    if i != ' ':
        if i.islower():
            temp += 'a'
        else:
            temp += 'b'
    if len(temp) == 5:
        temp_list.append(temp)
        temp = ''
for i in temp_list:
    if i in key:
        decoded_text += alphabet[key.find(i)]
print(decoded_text)        