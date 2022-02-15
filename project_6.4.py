def find_most_frequent(text):
    signs = [',','.',':','!','?',';','-']
    string_without_signs = ''
    for i in text:
        if i in signs:
            string_without_signs += ' '
        else:
            string_without_signs += i.lower()
    words_list = string_without_signs.split()
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
print(find_most_frequent('polsat,, polsa!?, karl'))