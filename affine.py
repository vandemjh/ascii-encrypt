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

# Given integers a and b
# finds d, s, and t such that
# d = a ∗ s + b ∗ t and d = gcd ( a , b )
def egcd (a , b):  #integers with a > b > 0
    s = 1 ; t = 0 ; u = 0 ; v = 1
    while b != 0:
        q = a / b
        a , b = b , a % b
        s , t , u , v = u , v , s - u * q , t - v * q
        d = a
    return d, s, t # as+b t = d and gcd ( a , b ) = d

def encrypt(input, a , b):
    if (math.gcd(a,b) != 1 or a < 1 or a > 127 or b < 1 or b > 127):
        print("The key pair (", a, ", ", b, ") is invalid, please select another key.")
        exit()
    toReturn = ""
    for char in input:
        # chr function changes value to ascii char
        # ord changes char to int value
        toReturn += chr(E(ord(char), a, b))
    return toReturn

def decrypt(input, a , b):
    if (math.gcd(a,b) != 1 or a < 1 or a > 127 or b < 1 or b > 127):
        print("The key pair (", a, ", ", b, ") is invalid, please select another key.")
        exit()
    toReturn = ""
    for char in input:
        toReturn += chr(D(ord(char), a, b))
    return toReturn


def decypher(input, output, dictionary):
    print (dictionary)

# --- Command Line Parsing ---#

if (len(sys.argv) != 6):
    print("Invalid number of arguments, 5 expected\n")
    exit()

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]
arg5 = sys.argv[5]

if (str(arg1) == "encrypt"):
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
    reader = open(str(arg2), "r")
    writer = open(str(arg3),"w")
    input = reader.read()
    a = int(arg4)
    b = int(arg5)
    decrypted = decrypt(input, a, b)
    writer.write(decrypted)
    reader.close()
    writer.close()
