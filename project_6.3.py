# Wrong solve
def saddle_point(matrix):
    index = 0
    for i in matrix:
        if max(i) != min(i):
            index = i.index(min(i))
            break
    list_of_value = []
    for numbers in matrix:
        min_number = min(numbers)
        if max(numbers) == min(numbers):
            list_of_value.append(min_number)
        elif numbers.count(min_number) != 1:
            return False
        elif numbers.index(min_number) != index:
            return False
        else:
            list_of_value.append(min_number)
    max_number = max(list_of_value)
    if list_of_value.count(max_number) != 1:
        return False
    else:
        index_point = (list_of_value.index(max_number), index)
        return index_point

m = [[4,4,6,3,7],[0,1,0,1,0],[6,5,7,8,9]]
print(saddle_point(m))
# Right solve:
def saddle_point(matrix):
    # перебір по зовнішньому списку
    for i in range(len(matrix)):
        # перебір по внутрішньому списку
        for j in range(len(matrix[i])):
            # нехай поточний елемент - сідлова точка
            flag = True
            ii = 0
            jj = 0
            # перевіримо, чи він є найбільшим в стовпці. якщо є хоч 1 ІНШИЙ елемент менший або рівний, то ні
            for ii in range(len(matrix)):
                if matrix[ii][j] >= matrix[i][j] and i != ii:
                    flag = False
            # перевіримо, чи він є найменшим в рядку. якщо є хоч 1 ІНШИЙ елемент більший або рівний, то ні
            for jj in range(len(matrix[i])):
                if matrix[i][jj] <= matrix[i][j] and j != jj:
                    flag = False
            # якщо всі умови виповнені, можна повертати відповідь
            if flag:
                return (i, j)
    # якщо цикли завершилися і ми досі нічого не повернули, сідлової точки немає
    return False