import sys
import math

# --- Function Definition ---#

# Given a character of our plaintext message m,
# the encryption function E(m, a, b) is given by:
# E(m, a, b) = (a · m + b) mod 128.
def E(m, a, b):
    return (a * m + b) % 128

def D(m, a, b):
    return (inverseMod(a, 128) * (m - b)) % 128

def inverseMod(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

def isValid(a, b):
    return (math.gcd(a, 128) != 1 or a < 1 or a > 127 or b < 1 or b > 127)

def encrypt(input, a , b):
    if (isValid(a, b)):
        print("The key pair (", a, ", ", b, ") is invalid, please select another key.")
        exit()
    toReturn = ""
    for char in input:
        # chr function changes value to ascii char
        # ord changes char to int value
        toReturn += chr(E(ord(char), a, b))
    return toReturn

def decrypt(input, a , b):
    if (isValid(a, b)):
        print("The key pair (", a, ", ", b, ") is invalid, please select another key.")
        exit()
    toReturn = ""
    for char in input:
        toReturn += chr(D(ord(char), a, b))
    return toReturn


def decypher(input, output, dictionary):
    print (dictionary)

# --- Command Line Parsing ---#

if (len(sys.argv) < 3):
    print("Invalid number of arguments")
    exit()

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]

if (str(arg1) == "encrypt"):
    arg5 = sys.argv[5]
    reader = open(str(arg2), "r")
    writer = open(str(arg3),"w")
    input = reader.read()
    a = int(arg4)
    b = int(arg5)
    encrypted = encrypt(input, a, b)
    writer.write(encrypted)
    reader.close()
    writer.close()

elif (str(arg1) == "decrypt"):
    arg5 = sys.argv[5]
    reader = open(str(arg2), "r")
    writer = open(str(arg3),"w")
    input = reader.read()
    a = int(arg4)
    b = int(arg5)
    decrypted = decrypt(input, a, b)
    writer.write(decrypted)
    reader.close()
    writer.close()

elif (str(arg1) == "decipher"):
    ciphertext = open(str(arg2), "r")
    ciphertext = ciphertext.read()
    output = open(str(arg3),"w")
    dictionary = open(str(arg4), "r")
    dictionary = dictionary.read()
    dictionary = dictionary.split("\n")
    maxWords = 0
    maxA = -1
    maxB = -1
    breaker = False
    for a in range(0, 128):
        if (breaker):
            break
        for b in range(0, 128):
            if (breaker):
                break
            if (not isValid(a, b)):
                deciphered = decrypt(ciphertext, a, b)
                decipheredSplit = deciphered.split();
                wordCount = 0
                for word in decipheredSplit:
                    #print(word)
                    if word in dictionary:
                        wordCount = wordCount + 1
                        if (maxWords <= wordCount):
                            maxWords = wordCount
                            maxA = a
                            maxB = b
                        #Tried a break out, unreliable
                        if (maxWords == len(decipheredSplit) and decipheredSplit[0] in dictionary and decipheredSplit[len(decipheredSplit) - 1] in dictionary):
                            print(maxWords)
                            print(decipheredSplit)
                            breaker = True
                            break

    if (maxA != -1 and maxB != -1):
        output.write(str(a-1))
        output.write(str(" "))
        output.write(str(b-1))
        output.write("\nDECIPHERED MESSAGE:\n")
        output.write(deciphered)
