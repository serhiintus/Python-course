#program decodes the message encoded with the Beacon's cipher
import sys

false_message = sys.argv[1]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
original_message = ''
ab_group = ''
groups = []

for i in false_message: 
    #remove spaces
    if i != ' ': 
        #replace characters with "a" and "b"
        if i.islower(): 
            ab_group += 'a'
        else:
            ab_group += 'b'
    #divide message into groups of 5 characters        
    if len(ab_group) == 5: 
        groups.append(ab_group)
        ab_group = ''
#replace ab-groups with alphabetic characters
for i in groups:
    if i in key:
        original_message += alphabet[key.find(i)] 
print(original_message)        