import sys

if (len(sys.argv) != 3):
    print("Invalid number of arguments, 2 expected")
    exit()

input = sys.argv[1]
output = sys.argv[2]

def encrypt(input, output):
    r = open(str(input), "r")
    w = open(str(output),"w")
    w.write(r);

print("Starting...")
encrypt(input, output)
