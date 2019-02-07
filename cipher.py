
upperList = list()
lowerList = list()


def inputStuff(typ, message, shiftNum, shiftDir, path):

    if typ == 1:
        message = message.split()
        return encode(message, shiftDir, shiftNum)

    elif typ == 2:
        rFile = open(path, "r")
        message = rFile.readline()
        rFile.close()
        message = message.split()
        return encode(message, shiftDir, shiftNum)

    elif typ == 3:
        message = message.split()
        return decode(message, shiftDir, shiftNum)

    elif typ == 4:
        rFile = open(path, "r")
        message = rFile.readline()
        rFile.close()
        return decode(message, shiftDir, shiftNum)


# Make list of uppercase characters
def generateUppercase():
    for upper in range(26):
        upperList.append(chr(upper + 65))


# Make list of lowercase characters
def generateLowercase():
    for lower in range(26):
        lowerList.append(chr(lower + 97))

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

    return newMessage


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

    return newMessage


