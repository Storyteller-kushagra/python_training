n = int(input())
for i in range(0, n):
    l = [int(x) for x in input().split()]
    for i in range(l[0] , l[1]+1):
        if i == 1:
            continue
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")