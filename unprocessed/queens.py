def sort(l):

    # if n == 1 or n == 0:
    #     return True
    # else:
        return l[0] < l[1] and sort(l[1:])

def making(n):

    l = []

    for i in range(n + 1):
        l.append(int(input(l)))

    print(sort(l))

making(5)