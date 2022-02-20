#Function gets a text string, and returns the string that contains the signal diagram 
#corresponding to the given text encoded by the international Morse code.
#Function ignore punctuation and characters that are not part of the Latin alphabet, and avoids letter case.
def encode_morze(text):
    morse_code = {
        "A" : ".-", 
        "B" : "-...", 
        "C" : "-.-.", 
        "D" : "-..", 
        "E" : ".", 
        "F" : "..-.", 
        "G" : "--.", 
        "H" : "....", 
        "I" : "..", 
        "J" : ".---", 
        "K" : "-.-", 
        "L" : ".-..", 
        "M" : "--", 
        "N" : "-.", 
        "O" : "---", 
        "P" : ".--.", 
        "Q" : "--.-", 
        "R" : ".-.", 
        "S" : "...", 
        "T" : "-", 
        "U" : "..-", 
        "V" : "...-", 
        "W" : ".--", 
        "X" : "-..-", 
        "Y" : "-.--", 
        "Z" : "--.."
        }
    if isinstance(text, str):
        text = text.upper()
        temp = text.split(' ')
        text_list = []
        for i in temp:
            if i != '':
                text_list.append(i)
        morse_signal = {}
        for i in morse_code:
            buf_1 = ''
            for j in morse_code[i]:
                if j == '.':
                    buf_1 += '^' + '_'
                else:
                    buf_1 += '^^^' + '_'
            morse_signal[i] = buf_1[:-1]
        signal_list = []
        for i in text_list:
            buf_2 = ''
            for j in i:
                if j in morse_signal:
                    buf_2 += morse_signal[j]
                    buf_2 += '___'
            signal_list.append(buf_2[:-3])
        return '_______'.join(signal_list)
