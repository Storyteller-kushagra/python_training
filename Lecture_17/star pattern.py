def starDown(stars):
    if stars == 0:
        return

    for i in range(stars):
        print("*", end=" ")

    print()
    starDown(stars - 1)

def starUp(stars):
    if stars == 0:
        return

    starUp(stars - 1)

    for i in range(stars):
        print("*", end=" ")

    print()

starUp(5)