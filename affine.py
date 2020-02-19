import sys

if (len(sys.argv) != 6):
    print("Invalid number of arguments, 5 expected\n")
    exit()

operation = sys.argv[1]
file1 = sys.argv[2]
file2 = sys.argv[3]
a = int(sys.argv[4])
b = int(sys.argv[5])

#TODO this
if (a % 2 == 0 or a < 1 or a > 127 or b < 1 or b > 127):
    print("The key pair (", a, ", ", b, ") is invalid, please select another key.")
    exit();

# Given a character of our plaintext message m,
# the encryption function E(m, a, b) is given by:
# E(m, a, b) = (a · m + b) mod 128.
def E(m, a, b):
    return (a * m + b) % 128

def D(a, m):
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
    toReturn = ""
    for char in input:
        # chr function changes value to ascii char
        # ord changes char to int value
        toReturn += chr(E(ord(char), a, b))
    return toReturn

def decrypt(input, a , b):
    toReturn = ""
    return toReturn

def decypher(input, output, dictionary):
    print dictionary

#print("Starting...")

reader = open(str(file1), "r")
writer = open(str(file2),"w")

input = reader.read()
#writer = output.write()

encrypted = encrypt(input, a, b)
#decrypted = decrypt(encrypted, 1, 1)

print (encrypted)
#print(decrypted)
