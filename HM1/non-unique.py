def non_unique(list):
    new_list = []
    for i in list:
       if list.count(i)>=2:
           new_list.append(i)
    return new_list

