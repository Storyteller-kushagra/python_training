def sub(processed, unprocessed):
    if len(unprocessed) == 0:
        print(processed)
        return
    ch = unprocessed[0]
    sub(processed + ch,  unprocessed[1:])
    sub(processed, unprocessed[1:])
def count_subseq(processed , unprocessed):
    if len(unprocessed) == 0:
        return 1
    ch = unprocessed[0]
    left = count_subseq(processed + ch ,  unprocessed[1:])
    right = count_subseq(processed, unprocessed[1:])
    return left+right
res = count_subseq("", "abc")
print(res)