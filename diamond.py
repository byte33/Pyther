def makediamond(string, width):
    width = int(width/2) + 1
    i = 0
    m = 0
    for line in range(width-1,-1,-1):
        letterCount = 0
        print(" "*line, end="")
        for x in range(0, i+1):
            print(string[x], end="")
            letterCount += 1
        for y in range(i):
            print(string[letterCount], end="")
            letterCount += 1
        print()
        i += 1
    actualWidth = letterCount
    i-=1
    for bottomLine in range(1, width):
        letterCount = 0

        print(" "*bottomLine, end="")
        for p in range(0, i):
            print(string[p], end="")
            letterCount += 1
        for y in range(i-1):
            print(string[letterCount], end="")
            letterCount += 1
        print()
        i -= 1


makediamond("yesmydiamond?yesmydiamond?yesmydiamond?yesmydiamond?yesmydiamond?yesmydiamond?yesmydiamond?yesmydiamond?yesmydiamond?", 100)

