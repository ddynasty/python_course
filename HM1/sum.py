def sum(list):
    sum = 0
    if list == []:
        print 0
    for i in list[::2]:
       sum += i
    return sum*list[-1]


