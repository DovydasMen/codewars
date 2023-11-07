def min_max(lst):
    min_max_list = []
    if len(lst) == 1:
        min_max_list.append([lst[0]])
        min_max_list.append([lst[0]])
        return min_max_list
    min_max_list.append(lst[0])
    min_max_list.append(lst[1])
    for item in lst:
        if item < min_max_list[0]:
            min_max_list[0] = item
        if item > min_max_list[1]:
            min_max_list[1] = item
    return min_max_list

print(min_max([1,2,3,4,5]))