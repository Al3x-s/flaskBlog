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
def generate_random_ip_address( ipclasslist):
    ips = []
    for i in ipclasslist: 
        if i == 'A':
            first_octet = random.randint(1, 126)
        elif i == 'B':
            first_octet = random.randint(128, 191)
        elif i == 'C':
            first_octet = random.randint(192, 223)
        elif i == 'D':
            first_octet = random.randint(224, 239)
        elif i == 'E':
            first_octet = random.randint(240, 255)
        ips.append(f"{first_octet}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}")
    return ips
  