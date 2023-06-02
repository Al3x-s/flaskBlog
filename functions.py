import random

def createRandomBinary():
    random_binary = ''
    for i in range(8):
        bit = random.randint(0,1)
        random_binary += str(bit)
    return random_binary
    #return String
    #DONE
####################################################
def fixBinary(given_num):
    if len(given_num) < 8: 
        difference = 8 - len(given_num)
        for i in range(difference):
            given_num = ''.join(('0',given_num))
        return(given_num)
    if len(given_num) > 8:
        given_num = given_num[-8:]
        return(given_num)
####################################################
def binaryToDecimal(binary_num):
    translated_binary = 0
    #binaryNum = binaryNum[::-1]
    start = 7
    for i in range(len(binary_num)):
        translated_binary += (2 ** start) * int(binary_num[i])
        start -= 1
    return translated_binary
####################################################