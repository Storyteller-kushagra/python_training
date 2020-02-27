def ret_lcs(first, second):
    if (len(first) == 0) or (len(second) == 0):
        return 0, ""
    if first[0] == second[0]:
        count, max_yet =  ret_lcs(first[1:], second[1:])
        return count + 1, first[0] + 