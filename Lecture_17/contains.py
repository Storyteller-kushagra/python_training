def lcs(first, second):
    if(len(first) == 0) or (len(second) == 0):
        return 0
    if first[0] == second[0]:
        return 1 + lcs(first[1:], second[1:])
    else:
        left = lcs(first[1:], second)
        right = lcs(first, second[1:])
        return max(left, right)

print(lcs("manan","aman")