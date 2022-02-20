#this function gets string of any length, which can contain Latin letters, spaces and punctuation marks (,.:;!?-"')
#and returns list of strings in lower case, which most often appear in the text
def find_most_frequent(text):
    marks = [',','.',':','!','?',';','-', '(', ')', '"', "'"]
    string_without_marks = ''
    for i in text:
        if i in marks:
            string_without_marks += ' '
        else:
            string_without_marks += i.lower()
    words_list = string_without_marks.split()
    if len(words_list) < 1:
        return words_list
    counted_words = {}
    for i in words_list:
        counted_words[i] = words_list.count(i)
    result = []
    max_count = max(counted_words.values())
    for i in counted_words:
        if counted_words[i] == max_count:
            result.append(i)
    result.sort()
    return result