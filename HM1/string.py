def most_frequent_letter(entered):

    entered=entered.lower()
    mass = []
    new_entered = ''
    re_entered = ''

    for i in entered:
        if i.isalpha() and not(i in new_entered):
            new_entered += i
    for i in new_entered:
        count = entered.count(i)
        mass.append(count)
        max_ident = max(mass)

    for i in range(len(mass)):
        if max_ident == mass[i]:
            re_entered += new_entered[i]
    return min(re_entered)



