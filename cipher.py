
upperList = list()
lowerList = list()


def inputStuff():
    try:
        typ = int(input("How would you like to enter the message?\n1 for manual entry(encode)\
        \n2 for file entry(encode)\n3 for manual entry(decode)\n4 for file entry(decode)\n"))
    except TypeError:
        typ = 1

    if typ == 1:
        message = input("Enter your message:\t")
        message = message.split()
        shiftNum, shiftDir = shiftOptions()
        encode(message, shiftDir, shiftNum)

    elif typ == 2:
        path = input("Please copy and paste the path to the file into the console.")
        rFile = open(path, "r")
        message = rFile.readline()
        rFile.close()
        message = message.split()
        shiftNum, shiftDir = shiftOptions()
        encode(message, shiftDir, shiftNum)

    elif typ == 3:
        message = input("Enter your message:\t")
        message = message.split()
        shiftNum, shiftDir = shiftOptions()
        cipher.decode(message, shiftDir, shiftNum)

    elif typ == 4:
        path = input("Please copy and paste the path to the file into the console.")
        rFile = open(path, "r")
        message = rFile.readline()
        rFile.close()
        message = message.split()
        shiftNum, shiftDir = shiftOptions()
        decode(message, shiftDir, shiftNum)

    else:
        print("Not a valid input")


# Make list of uppercase characters
def generateUppercase():
    for upper in range(26):
        upperList.append(chr(upper + 65))


# Make list of lowercase characters
def generateLowercase():
    for lower in range(26):
        lowerList.append(chr(lower + 97))


def shiftOptions():
    try:
        shiftNum = int(input("How much shift?\t"))
    except:
        shiftNum = 0

    shiftDir = input("In what direction? (L/R)\t")
    return shiftNum, shiftDir


# Main cipher goes here
def encode(message, shiftDir, shiftNum):
    newMessageList = list()
    newMessage = ""
    for word in message:
        letterList = []
        fullWord = ""
        for letter in word:
            if ord(letter) >= 65 and ord(letter) <= 90:
                if shiftDir == "L":
                    letterList.append(upperList[(upperList.index(letter) + shiftNum) % 26])
                elif shiftDir == "R":
                    letterList.append(upperList[(upperList.index(letter) - shiftNum) % 26])
            elif ord(letter) >= 97 and ord(letter) <= 122:
                if shiftDir == "L":
                    letterList.append(lowerList[(lowerList.index(letter) + shiftNum) % 26])
                elif shiftDir == "R":
                    letterList.append(lowerList[(lowerList.index(letter) - shiftNum) % 26])

        for finalLetter in letterList:
            fullWord = fullWord + finalLetter
        newMessageList.append(fullWord)

    for finalWord in newMessageList:
        newMessage = newMessage + finalWord + " "

    saveToFile(newMessage)


def decode(message, shiftDir, shiftNum):
    newMessageList = list()
    newMessage = ""
    for word in message:
        letterList = []
        fullWord = ""
        for letter in word:
            if ord(letter) >= 65 and ord(letter) <= 90:
                if shiftDir == "L":
                    letterList.append(upperList[(upperList.index(letter) - shiftNum) % 26])
                elif shiftDir == "R":
                    letterList.append(upperList[(upperList.index(letter) + shiftNum) % 26])
            elif ord(letter) >= 97 and ord(letter) <= 122:
                if shiftDir == "L":
                    letterList.append(lowerList[(lowerList.index(letter) - shiftNum) % 26])
                elif shiftDir == "R":
                    letterList.append(lowerList[(lowerList.index(letter) + shiftNum) % 26])

        for finalLetter in letterList:
            fullWord = fullWord + finalLetter
        newMessageList.append(fullWord)

    for finalWord in newMessageList:
        newMessage = newMessage + finalWord + " "

    saveToFile(newMessage)


def saveToFile(message):
    stf = input("Message has been encoded.  Store to file? (Y/N)")
    if stf == "Y":
        stfName = input("Please name the file")
        stfFile = open(stfName + ".txt", "w")
        stfFile.write(message)
        stfFile.close()
    else:
        print(message)
