def additional(clause):
    list4 = []
    if clause[0][1] != '0':
        if len(clause[0][0]) == 1:
            if len(clause[1][0]) != 1:
                if clause[0][1] != clause[1][1]:
                    list4.append((clause[0][1], clause[1][1]))
                else:
                    list4.append((clause[0][1], '0'))
            elif len(clause[1][1]) != 1:
                if clause[0][1] != clause[1][0]:
                    list4.append((clause[0][1], clause[1][0]))
                else:
                    list4.append((clause[0][1], '0'))
        elif len(clause[0][1]) == 1:
            if len(clause[1][0]) != 1 and clause[0][1] == clause[1][0][1]:
                if clause[0][0] != clause[1][1]:
                    list4.append((clause[0][0], clause[1][1]))
                else:
                    list4.append((clause[0][0], '0'))
            elif len(clause[1][1]) != 1 and clause[0][1] == clause[1][1][1]:
                if clause[0][0] != clause[1][0]:
                    list4.append((clause[0][0], clause[1][0]))
                else:
                    list4.append((clause[0][0], '0'))
    elif clause[1][1] != '0':
        if len(clause[0][0]) == 1:
            if len(clause[1][0]) != 1:
                list4.append((clause[1][1], '0'))
            elif len(clause[1][1]) != 1:
                list4.append((clause[1][0], '0'))
        elif len(clause[0][0]) != 1:
            if len(clause[1][0]) == 1:
                list4.append((clause[1][1], '0'))
            elif len(clause[1][1]) == 1:
                list4.append((clause[1][0], '0'))
    elif clause[1][1] == '0':
        if clause[0][0] == '~' + clause[1][0]:
            list4.append(('0', '0'))
        elif clause[1][0] == '~' + clause[0][0]:
            list4.append(('0', '0'))
    return list4

def is_satisfiable(cnf):
    cnf1 = cnf.replace(' ', '')
    cnf2 = cnf1.replace('(', '')
    cnf = cnf2.replace(')', '')
    list1 = list()
    list2 = list(cnf.split('/\\'))
    for i in list2:
        if '\\/' in i:
            a = i.split('\\/')[0]
            b = i.split('\\/')[1]
        elif '->' in i:
            a = i.split('->')[0]
            b = i.split('->')[1]
            if '~' in a:
                a = a.replace('~', '')
            else:
                a = '~' + a
        else:
            a = i
            b = '0'
        list1.append((a, b))
    print(list1)
    flag = False
    while flag is False:
            list3 = []
            for i, clause1 in enumerate(list1):
                for clause2 in list1[i + 1:]:
                    list3 = list3 + (additional([clause1, clause2]) + additional([clause2, clause1]))
                    if ('0', '0') in list3:
                        return False
            flag = set(list3).issubset(set(list1))
            list1 = list1 + list3
    return flag
cnf ="p /\\ (p -> q) /\\ (p -> ~r) /\\ (r \\/ ~s) /\\ (s \\/ ~q)"
print(is_satisfiable(cnf))