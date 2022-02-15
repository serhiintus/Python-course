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

arr = [  '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
print(file_search(arr, 'hereiam.py'))
