def starDownRec(row, col=0):
    if row == 0:
        return

    if col == row:
        print()
        starDownRec(row-1, 0)
        return

    print("*", end=" ")
    starDownRec(row, col+1)

starDownRec(5)