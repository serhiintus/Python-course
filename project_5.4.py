#this function gets two arguments - list 'folder' and string 'filename'
#and return string - full path to the file or folder 'filename' in the structure 'folder'
#example: 
#file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me']], 'hey.py'], 'find.me')
#return D:/tmp/new folder1/find.me
def file_search(folder, filename):
    if filename in folder[1:]:
        pth = [folder[0]]
        pth.append(filename)
        return '/'.join(pth)
    elif isinstance(folder, list) and len(folder) > 1:
        for i in folder[1:]:
            if file_search(i, filename):
                answ = [folder[0]]
                answ.append(file_search(i, filename))
                return '/'.join(answ)
    else:
        return False
    return False