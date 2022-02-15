def clean_list(list_to_clean):
    for i in range(len(list_to_clean) - 1):
        for j in range(i + 1, len(list_to_clean)):
            if list_to_clean[i] == list_to_clean[j] and isinstance(list_to_clean[i], type(list_to_clean[j])):
                list_to_clean[j] = None
    list_new = []
    for i in list_to_clean:
        if i != None:
            list_new.append(i)
    return list_new
l = ['qwest',222,222.002,'qwest',1,'qwest',222,'qwest',222,222.0,'222','qwes']
print(clean_list(l))