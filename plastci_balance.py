def plastic_balance(lst):
    on = True
    while on:
        if len(lst) == 1:
            if lst[0] + lst[0] != 0:
                return []
            else: 
                return lst
        if lst == []:
            return []
        if lst[0] + lst[-1] != sum(lst[1:-1]):
            del lst[0]
            del lst[-1]
            continue
        if lst[0] + lst[-1] == sum(lst[1:-1]):
            return lst
    


print(plastic_balance([0,104,3,101,0,111]))