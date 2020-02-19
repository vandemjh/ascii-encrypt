import sys

if (len(sys.argv) != 3):
    print("Invalid number of arguments, 2 expected")
    exit()

input = sys.argv[1]
output = sys.argv[2]


# Given a character of our plaintext message m,
# the encryption function E(m, a, b) is given by:
# E(m, a, b) = (a · m + b) mod 128.
def E(m, a, b):
    return (a * m + b) % 128

def encrypt(input, a , b):
    toReturn = ""
    for char in input:
        # chr function changes value to ascii char
        # ord changes char to int value
        toReturn += chr(E(ord(char), a, b))
    return toReturn

def decrypt(input, output, a , b):
    toReturn = ""
    for char in input:
        toReturn += chr(E(ord(char), a, b))
    return toReturn

#print("Starting...")

reader = open(str(input), "r")
writer = open(str(output),"w")

input = reader.read()
#writer = output.write()

encrypted = encrypt(input, 1, 1)
#decrypted = decrypt(output, input)

print (encrypted)
